# scoring/serializers.py
from rest_framework import serializers
from .models import Score

class ScoreSerializer(serializers.ModelSerializer):
    """
    Used by judges to submit scores.
    """

    class Meta:
        model = Score
        fields = [
            'id',
            'match',
            'participant_name',
            'points',
            'created_at'
        ]

    def validate_points(self, value):
        """
        Ensures score is non-negative.
        """
        if value < 0:
            raise serializers.ValidationError("Score cannot be negative.")
        return value
