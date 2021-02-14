from django.urls import path

from . import views

app_name = 'profile'
urlpatterns = [
    path('user/<pk>', views.UserUpdate.as_view(), name='user'),
    path('user/<pk>/profile', views.ProfileUpdate.as_view(), name='profile'),
]
