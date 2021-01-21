from django.urls import path, include

from . import views

app_name = 'main'
urlpatterns = [
    path('pages/', include('django.contrib.flatpages.urls')),
    path('', views.index, name='index'),
]
