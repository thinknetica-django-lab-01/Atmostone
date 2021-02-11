from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, TemplateView

from apps.main.models import Hotel, HotelFeature


class MainpageView(TemplateView):
    template_name = "main/index.html"


class HotelList(ListView):
    """View for hotel list"""
    model = Hotel
    paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hotel_features'] = HotelFeature.objects.all()
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        features = self.request.GET.get("features")
        if features:
            queryset = Hotel.objects.filter(features__title=features)

        return queryset


class HotelDetail(DetailView):
    """View for hotel details"""
    model = Hotel


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
