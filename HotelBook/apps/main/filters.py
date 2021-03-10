import django_filters
from rest_framework.pagination import PageNumberPagination

from apps.main.models import Hotel


class DebugResultsSetPagination(PageNumberPagination):
    page_size = 1


class HotelFilter(django_filters.FilterSet):
    class Meta:
        model = Hotel
        fields = {
            'title': ['icontains'],
            'city__title': ['icontains'],
            'stars': ['exact'],
            'rating': ['gt'],
            'features__title': ['icontains'],
        }
