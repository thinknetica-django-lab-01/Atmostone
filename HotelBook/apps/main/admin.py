from ckeditor.widgets import CKEditorWidget
from django import forms
from django.contrib import admin

from django.contrib.flatpages.models import FlatPage

from apps.main.models import Country, City, RoomFeature, Hotel, Room, Order


class FlatPageAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = FlatPage
        fields = '__all__'


class FlatPageAdmin(admin.ModelAdmin):
    form = FlatPageAdminForm


class HotelAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'stars', 'rating', 'active')
    readonly_fields = ('created_at',)
    list_filter = ('features', 'created_at', 'stars')
    search_fields = ('title',)
    actions = ('make_active', 'make_inactive')

    def location(self, obj):
        return f'{obj.city}. {obj.city.country}'

    location.short_description = 'Location'

    def make_active(self, request, queryset):
        queryset.update(active=True)

    make_active.short_description = 'Make selected hotels visible'

    def make_inactive(self, request, queryset):
        queryset.update(active=False)

    make_inactive.short_description = 'Make selected hotels not visible'


admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)

admin.site.register(Country)
admin.site.register(City)
admin.site.register(RoomFeature)
admin.site.register(Room)
admin.site.register(Order)

admin.site.register(Hotel, HotelAdmin)
