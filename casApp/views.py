from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators. csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from casApp.models import Casa, Event, Location, User, Class, Group, Date, Teacher
from casApp.serializers import EventSerializer, LocationSerializer, UserSerializer, CasaSerializer, GroupSerializer
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
            return JsonResponse({'status': 'false', 'message': 'Missing fields'}, status=400)
        try:
            casa = Casa.objects.get(name=casa_name)
        except Casa.DoesNotExist:
            return JsonResponse({'status': 'false', 'message': 'Casa doesnt exist'}, status=404)
        if len(User.objects.filter(mat=mat)) > 0:
            return JsonResponse({'status': 'false', 'message': f'User with {mat} already exists. Use PUT to update'}, status=405)
        user = User(name=name, mat=mat, password=password, casa=casa)
        user.save()
        serializer = UserSerializer(user)
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def student_detail(request, mat):
    """Render student details html."""
    if request.method == 'GET':
        try:
            user = User.objects.get(mat=mat)
        except User.DoesNotExist:
            return JsonResponse({'status': 'false', 'message': 'User does not exist'}, status=403)
        groups = user.enrolled_in.all()
        serializer = GroupSerializer(groups, many=True)
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def login(request):
    if request.method == 'POST':
        try:
            body = json.loads(request.body.decode("utf-8"))
            mat = body['mat']
            password = body['password']
        except KeyError:
            return JsonResponse({'status': 'false', 'message': 'Missing fields'}, status=400)
        try:
            user = User.objects.get(mat=mat, password=password)
        except User.DoesNotExist:
            return JsonResponse({'status': 'false', 'message': 'User does not exist or wrong password'}, status=403)
        serializer = UserSerializer(user)
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def get_events(request):
    if request.method == 'GET':
        next_events = [event for event in Event.objects.all() if event.date >= timezone.now()]
        sorted_events = sorted(next_events, key=lambda event: event.date)
        serializer = EventSerializer(sorted_events, many=True)
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def add_event(request):
    if request.method == 'POST':
        try:
            body = json.loads(request.body.decode("utf-8"))
            mat = body['mat']
            event_id = body['event_id']
        except KeyError:
            return JsonResponse({'status': 'false', 'message': 'Missing fields'}, status=400)
        try:
            user = User.objects.get(mat=mat)
        except User.DoesNotExist:
            return JsonResponse({'status': 'false', 'message': 'User does not exist'}, status=404)
        try:
            event = Event.objects.get(id=event_id)
        except Event.DoesNotExist:
            return JsonResponse({'status': 'false', 'message': 'Event does not exist'}, status=404)
        user.events.add(event)
        serializer = UserSerializer(user)
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def remove_event(request):
    if request.method == 'POST':
        try:
            body = json.loads(request.body.decode("utf-8"))
            mat = body['mat']
            event_id = body['event_id']
        except KeyError:
            return JsonResponse({'status': 'false', 'message': 'Missing fields'}, status=400)
        try:
            user = User.objects.get(mat=mat)
        except User.DoesNotExist:
            return JsonResponse({'status': 'false', 'message': 'User does not exist'}, status=404)
        try:
            event = Event.objects.get(id=event_id)
        except Event.DoesNotExist:
            return JsonResponse({'status': 'false', 'message': 'Event does not exist'}, status=404)
        user.events.remove(event)
        serializer = UserSerializer(user)
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def get_all_events(request):
    if request.method == 'GET':
        events = Event.objects.all()
        sorted_events = sorted(events, key=lambda event: event.date)
        serializer = EventSerializer(sorted_events, many=True)
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


@csrf_exempt
def add_class(request):
    if request.method == 'POST':
        try:
            body = json.loads(request.body.decode("utf-8"))
            mat = body['mat']
            classes = body['horario']
        except KeyError:
            return JsonResponse({'status': 'false', 'message': 'Missing fields'}, status=400)
        try:
            user = User.objects.get(mat=mat)
        except User.DoesNotExist:
            return JsonResponse({'status': 'false', 'message': 'User does not exist'}, status=404)
        try:
            for cl in classes:
                print(cl_string)
                class_json = cl['class_id']
                class_id = class_json['class_id']
                class_name = class_json['class_name']
                group_number = cl['group_number']
                try:
                    current_class = Class.objects.get(class_id=class_id)
                except ObjectDoesNotExist:
                    current_class = Class(class_id=class_id, class_name=class_name)
                    current_class.save()
                try:
                    group = Group.objects.get(class_id=current_class, group_number=group_number)
                except ObjectDoesNotExist:
                    group = Group(class_id=current_class,
                                  group_number=group_number, semester='EM2019')
                    group.save()
                    teachers = cl['teachers']
                    for teacher_string in teachers:
                        try:
                            teacher = Teacher.objects.get(teacher_name=teacher_string)
                        except ObjectDoesNotExist:
                            teacher = Teacher(teacher_name=teacher_string)
                            teacher.save()
                        group.teachers.add(teacher)
                    dates = cl['dates']
                    days = {'Domingo': 0, 'Lunes': 1, 'Martes': 2,
                            'Miercoles': 3, 'Jueves': 4, 'Viernes': 5, 'Sabado': 6}
                    for date_string in dates:
                        [day, time] = date_string.split(' a las ')
                        possible_dates = Date.objects.filter(day=days[day])
                        try:
                            group.dates.add(
                                [date for date in possible_dates if str(date) == date_string][0])
                        except IndexError:
                            return JsonResponse({'status': 'false', 'message': 'Wrong date format'}, status=400)
                user.enrolled_in.add(group)
        except KeyError:
            return JsonResponse({'status': 'false', 'message': 'Missing fields'}, status=400)
        serializer = UserSerializer(user)
        return JsonResponse(serializer.data, safe=False)
