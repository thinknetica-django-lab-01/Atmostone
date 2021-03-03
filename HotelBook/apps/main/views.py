from django.core.cache import cache
from django.views.generic import ListView, DetailView, \
    CreateView, UpdateView, TemplateView

from apps.main.models import Hotel


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
        print(context['hotel_features'])
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        feature = self.request.GET.get("features")
        print(feature)
        #print(Hotel.objects.filter(features__contains=[feature]).query)
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
