from rest_framework import serializers
from casApp.models import Casa, Event, Location, User, Group


class UserSerializer(serializers.ModelSerializer):
    casa = serializers.StringRelatedField(read_only=True)
    events = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('name', 'mat', 'casa', 'events')


class EventSerializer(serializers.ModelSerializer):
    date = serializers.DateTimeField(format="%B/%d/%Y, %H:%M", read_only=True)

    class Meta:
        model = Event
        fields = ('id', 'name', 'description', 'location', 'date')


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('id', 'name', 'maps', 'photo')


class CasaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Casa
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    class_id = serializers.StringRelatedField()
    teachers = serializers.StringRelatedField(many=True)
    dates = serializers.StringRelatedField(many=True)

    class Meta:
        model = Group
        fields = ('class_id', 'group_number', 'teachers', 'dates')
