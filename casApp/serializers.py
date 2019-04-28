from rest_framework import serializers
from casApp.models import Casa, Event, Location, User


class UserSerializer(serializers.ModelSerializer):
    casa = serializers.StringRelatedField(read_only=True)
    events = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('name', 'mat', 'casa', 'events')


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'name', 'description', 'location')


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('id', 'name', 'maps', 'photo')


class CasaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Casa
        fields = '__all__'
