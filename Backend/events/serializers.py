from rest_framework import serializers
from .models import Event, Venue, RoundTemplate

class VenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venue
        fields = ['id', 'name', 'location']

class EventSerializer(serializers.ModelSerializer):
    venue = VenueSerializer()
    
    class Meta:
        model = Event
        fields = ['id', 'name', 'venue', 'coordinator', 'is_group_event', 'is_active']

class RoundTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoundTemplate
        fields = ['id', 'name', 'description']