# matches/models.py
from django.db import models
from events.models import Event

class Match(models.Model):
    """
    Represents a single match in a specific round.
    """
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    round_name = models.CharField(max_length=50)
    start_time = models.DateTimeField()
    venue = models.CharField(max_length=100)

    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.event.name} - {self.round_name}"


class MatchOpponent(models.Model):
    """
    Links participants to a match.
    Supports individual & team events.
    """
    match = models.ForeignKey(
        Match,
        related_name='opponents',
        on_delete=models.CASCADE
    )
    participant_name = models.CharField(max_length=100)
    is_winner = models.BooleanField(default=False)

    def __str__(self):
        return self.participant_name
