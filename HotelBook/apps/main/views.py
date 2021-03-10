from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from django.core.cache import cache
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from django.views.generic import ListView, DetailView, \
    CreateView, UpdateView, TemplateView
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated

from apps.main.filters import HotelFilter, DebugResultsSetPagination
from apps.main.models import Hotel
from apps.main.permissions import IsOwnerOrReadOnly
from apps.main.serializers import HotelSerializer


class MainpageView(TemplateView):
    template_name = "main/index.html"


class HotelList(ListView):
    """View for hotel list"""
    model = Hotel
    paginate_by = 3

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        features = set()
        for hotel in Hotel.objects.all():
            features.update(hotel.features)
        context['hotel_features'] = features
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        feature = self.request.GET.get("features")
        if feature:
            queryset = Hotel.objects.filter(features__contains=[feature])
        return queryset


class HotelDetail(DetailView):
    """View for hotel details"""
    model = Hotel

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        self.object.views += 1
        self.object.save()
        context['views'] = cache.get_or_set(f'{self.object.pk}'
                                            + '_views', self.object.views, 5)
        return context


class HotelCreate(CreateView):
    """View for creating hotels"""
    model = Hotel
    fields = '__all__'
    success_url = '/hotels/'


class HotelUpdate(UpdateView):
    """View for updating hotels"""
    model = Hotel
    fields = '__all__'
    success_url = '/hotels/'


class HotelSearch(ListView):
    """View for searching hotels"""
    model = Hotel
    template_name = 'main/hotel_search.html'
    context_object_name = 'object_list'

    def get_queryset(self):
        result = super(HotelSearch, self).get_queryset()
        query = self.request.GET.get('search')
        if query:
            vector = SearchVector('title', 'description')
            search_query = SearchQuery(query)
            result = Hotel.objects.annotate(rank=SearchRank(vector, search_query)).filter(rank__gte=0.001).order_by(
                '-rank')
        return result


class HotelViewSet(viewsets.ModelViewSet):
    """
    API Viewset for list, create, update and delete hotels
    """
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    pagination_class = DebugResultsSetPagination
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = HotelFilter
    ordering = ['-created_at']

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
        return [permission() for permission in permission_classes]
