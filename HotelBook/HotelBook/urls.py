from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import path, include

from apps.main.sitemap import HotelSitemap

sitemaps = {
    'hotels': HotelSitemap,
}

urlpatterns = [
    path('pages/', include('django.contrib.flatpages.urls')),
    path('', include('apps.main.urls')),
    path('account/', include('allauth.urls')),
    path('profile/', include('apps.profile.urls')),
    path('admin/', admin.site.urls),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap')

]
