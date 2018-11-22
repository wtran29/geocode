from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings

# DESTINATION_CHOICES = (
#     ('from', 'From'),
#     ('to', 'To'),
# )


# class Coordinate(models.Model):
#     name = models.CharField(max_length=250, blank=True)
#     address = models.CharField(max_length=255)
#     # destination = models.CharField(max_length=120, choices=DESTINATION_CHOICES)
#     longitude = models.DecimalField(decimal_places=7, max_digits=1000)
#     latitude = models.DecimalField(decimal_places=7, max_digits=1000)
#
#     def __str__(self):
#         return str(self.latitude) + ", " + str(self.longitude)
    # @property
    # def longitude(self):
    #     return self.point[0]
    #
    # @property
    # def latitude(self):
    #     return self.point[1]

class LocationManager(models.Manager):
    # handle the logic here
    pass


# Not the best way to create the model but I wanted the coordinates
# together as one id to calculate distance for rest framework
class Location(models.Model):
    loc_name = models.CharField(max_length=250, blank=True)
    loc_address = models.CharField(max_length=255, null=True)
    lat1 = models.DecimalField(decimal_places=7, max_digits=1000, null=True)
    lng1 = models.DecimalField(decimal_places=7, max_digits=1000, null=True)
    dest_name = models.CharField(max_length=250, blank=True)
    dest_address = models.CharField(max_length=255, null=True)
    # destination = models.CharField(max_length=120, blank=True, choices=DESTINATION_CHOICES)
    lat2 = models.DecimalField(decimal_places=7, max_digits=1000, null=True)
    lng2 = models.DecimalField(decimal_places=7, max_digits=1000, null=True)
    # geo_distance = models.FloatField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.lat1) + ", " + str(self.lng1)

    objects = LocationManager()



