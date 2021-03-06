from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from apps.main.models import Hotel


class HotelSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.9

    def items(self):
        return Hotel.objects.all()

    def location(self, item):
        return f'/hotels/{item.pk}'
