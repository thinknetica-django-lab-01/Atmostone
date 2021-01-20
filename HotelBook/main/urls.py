from django.urls import path, include

from . import views

urlpatterns = [
    path('pages/', include('django.contrib.flatpages.urls')),
    path('', views.index, name='index'),
]
