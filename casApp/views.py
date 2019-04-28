from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators. csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from casApp.models import Casa, Event, Location, User
from casApp.serializers import EventSerializer, LocationSerializer, UserSerializer, CasaSerializer
from datetime import datetime
import json
from django.utils import timezone


# Create your views here.


@csrf_exempt
def user(request):
    if request.method == 'POST':
        try:
            body = json.loads(request.body.decode("utf-8"))
            name = body['name']
            mat = body['mat']
            password = body['password']
            casa_name = body['casa']
        except KeyError:
            return JsonResponse({'status': 'false', 'message': 'Missing fields'})
        try:
            casa = Casa.objects.get(name=casa_name)
        except Casa.DoesNotExist:
            return JsonResponse({'status': 'false', 'message': 'Casa doesnt exist'})
        if len(User.objects.filter(mat=mat)) > 0:
            return JsonResponse({'status': 'false', 'message': f'User with {mat} already exists. Use PUT to update'})
        user = User(name=name, mat=mat, password=password, casa=casa)
        user.save()
        serializer = UserSerializer(user)
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def login(request):
    if request.method == 'GET':
        try:
            body = json.loads(request.body.decode("utf-8"))
            mat = body['mat']
            password = body['password']
        except KeyError:
            return JsonResponse({'status': 'false', 'message': 'Missing fields'})
        try:
            user = User.objects.get(mat=mat, password=password)
        except User.DoesNotExist:
            return JsonResponse({'status': 'false', 'message': 'User does not exist or wrong password'})
        serializer = UserSerializer(user)
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def get_events(request):
    if request.method == 'GET':
        events = Event.objects.all()
        serializer = EventSerializer(
            [event for event in events if event.date >= timezone.now()], many=True)
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def get_locations(request):
    if request.method == 'GET':
        locations = Location.objects.all()
        serializer = LocationSerializer(locations, many=True)
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def get_casas(request):
    if request.method == 'GET':
        casas = Casa.objects.all()
        serializer = CasaSerializer(casas, many=True)
        return JsonResponse(serializer.data, safe=False)
