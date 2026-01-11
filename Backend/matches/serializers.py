# matches/serializers.py
from rest_framework import serializers
from .models import Match, MatchOpponent

class MatchOpponentSerializer(serializers.ModelSerializer):
    class Meta:
        model = MatchOpponent
        fields = ['id', 'participant_name', 'is_winner']


class MatchSerializer(serializers.ModelSerializer):
    opponents = MatchOpponentSerializer(many=True, read_only=True)

    class Meta:
        model = Match
        fields = [
            'id',
            'event',
            'round_name',
            'start_time',
            'venue',
            'is_completed',
            'opponents'
        ]
