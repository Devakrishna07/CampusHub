# registration/serializers.py
from rest_framework import serializers
from .models import Registration

class RegistrationSerializer(serializers.ModelSerializer):
    """
    Used for public event registration.
    """

    class Meta:
        model = Registration
        fields = [
            'id',
            'participant_name',
            'house',
            'event',
            'created_at'
        ]

    def validate(self, data):
        """
        Prevent duplicate registrations for the same event.
        """
        if Registration.objects.filter(
            participant_name=data['participant_name'],
            event=data['event']
        ).exists():
            raise serializers.ValidationError(
                "Participant already registered for this event."
            )
        return data
