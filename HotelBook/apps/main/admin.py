from ckeditor.widgets import CKEditorWidget
from django import forms
from django.contrib import admin

from django.contrib.flatpages.models import FlatPage

from apps.main.models import Country, City,\
    HotelFeature, RoomFeature, Hotel, Room, Order


class FlatPageAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = FlatPage
        fields = '__all__'


class FlatPageAdmin(admin.ModelAdmin):
    form = FlatPageAdminForm


class HotelAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)


admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)

admin.site.register(Country)
admin.site.register(City)
admin.site.register(HotelFeature)
admin.site.register(RoomFeature)
admin.site.register(Room)
admin.site.register(Order)

admin.site.register(Hotel, HotelAdmin)
