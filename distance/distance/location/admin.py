from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# from django.contrib.gis.geos import GEOSGeometry
from distance.location.models import Location  # Coordinate


class LocationAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'latitude', 'longitude']
    search_fields = ['name', 'address']


admin.site.register(Location, LocationAdmin)
# admin.site.register(Coordinate)
