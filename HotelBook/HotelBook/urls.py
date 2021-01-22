from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('pages/', include('django.contrib.flatpages.urls')),
    path('', include('apps.main.urls')),
    path('admin/', admin.site.urls),
]
