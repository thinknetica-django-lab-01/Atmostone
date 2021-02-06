from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from apps.main.models import Hotel, HotelFeature


def index(request):
    user = request.user
    if user.profile.status == 'O':
        is_owner = True
    else:
        is_owner = False

    context = {
        'user': user,
        'is_owner': is_owner,
    }
    return render(request, 'main/index.html', context)


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


class HotelDetail(DetailView):
    model = Hotel


class HotelCreate(CreateView):
    model = Hotel
    fields = '__all__'
    success_url = '/hotels/'


class HotelUpdate(UpdateView):
    model = Hotel
    fields = '__all__'
    success_url = '/hotels/'
