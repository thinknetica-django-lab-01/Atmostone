from django.conf.urls import url
from django.urls import path

from . import views


def trigger_error(request):
    return 1 / 0


app_name = 'main'
urlpatterns = [
    path('hotels/add', views.HotelCreate.as_view(), name='hotel_create'),
    path('hotels/<int:pk>', views.HotelDetail.as_view(), name='hotel_detail'),
    path('hotels/<int:pk>/edit', views.HotelUpdate.as_view(),
         name='hotel_update'),
    path('hotels/', views.HotelList.as_view(), name='hotel_list'),
    path('hotels/search/', views.HotelSearch.as_view(), name='hotel_search'),
    path('sentry_debug/', trigger_error),
    path('', views.MainpageView.as_view(), name='index'),
]
