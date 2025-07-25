from rest_framework import serializers
from .models import EventPoster

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventPoster
        fields = '__all__'