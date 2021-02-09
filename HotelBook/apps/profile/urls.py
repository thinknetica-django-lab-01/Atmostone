from django.urls import path

from . import views

app_name = 'profile'
urlpatterns = [
    path('user/<pk>', views.ProfileUpdate.as_view(), name='profile'),
]