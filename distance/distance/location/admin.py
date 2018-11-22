from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# from django.contrib.gis.geos import GEOSGeometry
from distance.location.models import Location  # Coordinate


class LocationAdmin(admin.ModelAdmin):
    list_display = ['loc_name', 'loc_address', 'lat1', 'lng1',
                    'dest_name', 'dest_address', 'lat2', 'lng2']
    search_fields = ['loc_address', 'dest_address']

    class Meta:
        model = Location


admin.site.register(Location, LocationAdmin)
# admin.site.register(Coordinate)
