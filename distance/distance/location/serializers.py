from rest_framework.serializers import ModelSerializer
from distance.location.models import Location


class LocationSerializer(ModelSerializer):

    class Meta:
        model = Location
        fields = (
            'id',
            'loc_name',
            'loc_address',
            'lat1',
            'lng1',
            'dest_name',
            'dest_address',
            'lat2',
            'lng2',
            # 'geo_distance',
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
