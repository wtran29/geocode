from django.shortcuts import render, redirect
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from django.http import JsonResponse, HttpResponse
from django.conf import settings
from django.core import serializers
import json
import re
import requests
from rest_framework.viewsets import ModelViewSet
from distance.location.models import Location
from distance.location.serializers import LocationSerializer
import math


URL = "https://maps.googleapis.com/maps/api/geocode/json?"


def calculate_distance(lat1, lng1, lat2, lng2):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    """
    lat1, lng1, lat2, lng2 = map(math.radians, [lat1, lng1, lat2, lng2])

    # haversine formula
    dlng = lng2 - lng1
    dlat = lat2 - lat1
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlng / 2) ** 2
    c = 2 * math.asin(math.sqrt(a))
    r = 3956  # Radius of earth in 6371 kilometers. Use 3956 for miles
    distance = c * r
    return distance


def get_location(request):
    if request.POST.get('location') == '' or request.POST.get('destination') == '':
        return redirect('/')
    else:
        if request.POST == 'POST' and request.POST.get('location'):
            # Location.objects.destination.save('location', 'from')
            if re.match(r'^(\-?\d+(\.\d+)?),\s*(\-?\d+(\.\d+)?)$', request.POST):

                coordinates = re.match(r'^(\-?\d+(\.\d+)?),\s*(\-?\d+(\.\d+)?)$', request.POST.get('location'))
                latlng = coordinates.group()
                reverse_geocode = URL + "latlng=" + latlng + "&key=" + settings.YOUR_API_KEY
                response = requests.get(reverse_geocode)
                json_payload = response.json()
                print(json_payload['results'][0]['geometry']['location'])
                lat1 = json_payload['results'][0]['geometry']['location']['lat']

                lng1 = json_payload['results'][0]['geometry']['location']['lng']

                loc_address = json_payload['results'][0]['formatted_address']

        else:
            # Location.objects.destination.save('location', 'from')
            geocode = URL + "address=" + request.POST.get('location') + "&key=" + settings.YOUR_API_KEY
            response = requests.get(geocode)
            json_payload = response.json()
            print(json_payload['results'][0]['geometry']['location'])
            lat1 = json_payload['results'][0]['geometry']['location']['lat']

            lng1 = json_payload['results'][0]['geometry']['location']['lng']

            loc_address = json_payload['results'][0]['formatted_address']

        Location.objects.create(address=loc_address, latitude=lat1, longitude=lng1, destination='from')

        if request.POST == 'POST' and request.POST.get('destination'):
            # Location.objects.destination.save('destination', 'to')
            if re.match(r'^(\-?\d+(\.\d+)?),\s*(\-?\d+(\.\d+)?)$', request.POST):
                coordinates = re.match(r'^(\-?\d+(\.\d+)?),\s*(\-?\d+(\.\d+)?)$', request.POST.get('destination'))
                latlng = coordinates.group()
                reverse_geocode = URL + "latlng=" + latlng + "&key=" + settings.YOUR_API_KEY
                response = requests.get(reverse_geocode)
                json_payload = response.json()
                print(json_payload['results'][0]['geometry']['location'])
                lat2 = json_payload['results'][0]['geometry']['location']['lat']

                lng2 = json_payload['results'][0]['geometry']['location']['lng']

                dest_address = json_payload['results'][0]['formatted_address']

        else:
            # Location.objects.destination.save('destination', 'to')
            geocode = URL + "address=" + request.POST.get('destination') + "&key=" + settings.YOUR_API_KEY
            response = requests.get(geocode)
            json_payload = response.json()
            print(json_payload['results'][0]['geometry']['location'])
            lat2 = json_payload['results'][0]['geometry']['location']['lat']
            lng2 = json_payload['results'][0]['geometry']['location']['lng']
            dest_address = json_payload['results'][0]['formatted_address']
        Location.objects.create(address=dest_address, latitude=lat2, longitude=lng2, destination='to')
    distance = calculate_distance(lat1, lng1, lat2, lng2)
    context = {
        'location': loc_address,
        'destination': dest_address,
        'distance': round(distance, 2),

    }
    return render(request, 'index.html', context)


def home_page(request):
    return render(request, 'index.html')


class LocationViewSet(ModelViewSet):
    # queryset = Location.objects.all()
    serializer_class = LocationSerializer

    def get_queryset(self):
        from_destination = Location.objects.filter(destination='from')
        return from_destination

    def list(self, request, *args, **kwargs):
        locations = Location.objects.filter(id=1)
        serializer = LocationSerializer(locations, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        obj = Location.objects.get(id=kwargs['pk'])
        serializer = LocationSerializer(obj)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        data = request.data
        location = Location.objects.create(
            
        )