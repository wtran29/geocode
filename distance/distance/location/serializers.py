from rest_framework.serializers import ModelSerializer
from distance.location.models import Location


class LocationSerializer(ModelSerializer):

    class Meta:
        model = Location
        fields = (
            'id',
            'name',
            'address',
            'latitude',
            'longitude',
        )

#
# class CoordinateSerializer(ModelSerializer):
#
#     class Meta:
#         model = Coordinate
#         fields = (
#             'id',
#             'latitude',
#             'longitude',
#         )
#
