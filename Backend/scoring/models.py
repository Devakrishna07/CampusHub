# scoring/models.py
from django.db import models
from matches.models import Match

class Score(models.Model):
    """
    Stores score given to a participant in a match.
    Used for both individual and group events.
    """

    match = models.ForeignKey(
        Match,
        on_delete=models.CASCADE,
        related_name='scores'
    )

    participant_name = models.CharField(
        max_length=100,
        help_text="Individual or team name"
    )

    points = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('match', 'participant_name')

    def __str__(self):
        return f"{self.participant_name} - {self.points}"
