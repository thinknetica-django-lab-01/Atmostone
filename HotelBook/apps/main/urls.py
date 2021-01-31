from django.urls import path

from . import views

app_name = 'main'
urlpatterns = [
    path('hotels/', views.HotelList.as_view(), name='hotels'),
    path('hotel/<int:pk>', views.HotelDetail.as_view(), name='hotel_detail'),
    path('', views.index, name='index'),
]
