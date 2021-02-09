from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, TemplateView

from apps.main.models import Hotel, HotelFeature


class MainpageView(TemplateView):
    template_name = "main/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context


class HotelList(ListView):
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


# View for hotel details
class HotelDetail(DetailView):
    model = Hotel


# View for creating hotels
class HotelCreate(CreateView):
    model = Hotel
    fields = '__all__'
    success_url = '/hotels/'


# View for updating hotels
class HotelUpdate(UpdateView):
    model = Hotel
    fields = '__all__'
    success_url = '/hotels/'
