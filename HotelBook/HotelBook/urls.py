from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import path, include

from rest_framework import routers
from apps.main import views
from apps.main.sitemap import HotelSitemap

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

sitemaps = {
    'hotels': HotelSitemap,
}

urlpatterns = [
    path('pages/', include('django.contrib.flatpages.urls')),
    path('', include('apps.main.urls')),
    path('account/', include('allauth.urls')),
    path('profile/', include('apps.profile.urls')),
    path('admin/', admin.site.urls),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
