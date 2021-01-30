from django.shortcuts import render
from django.views.generic import ListView, DetailView

from apps.main.models import Hotel, HotelFeature


def index(request):
    user = request.user
    if user.status == 'O':
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

    # def get_queryset(self):
    #   print(self.kwargs)
    #  self.features = get_object_or_404(HotelFeature, title=self.kwargs['features'])
    # return Hotel.objects.filter(features=self.features)


class HotelDetail(DetailView):
    model = Hotel
