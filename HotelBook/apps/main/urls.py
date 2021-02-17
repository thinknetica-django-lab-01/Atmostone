from django.urls import path
from django.views.decorators.cache import cache_page

from . import views

app_name = 'main'
urlpatterns = [
    path('hotels/', views.HotelList.as_view(), name='hotel_list'),
    path('hotels/add', views.HotelCreate.as_view(), name='hotel_create'),
    path('hotels/<int:pk>', cache_page(60)(views.HotelDetail.as_view()), name='hotel_detail'),
    path('hotels/<int:pk>/edit', views.HotelUpdate.as_view(), name='hotel_update'),
    path('', views.MainpageView.as_view(), name='index'),
]
