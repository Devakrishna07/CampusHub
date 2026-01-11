# registration/models.py
from django.db import models
from events.models import Event

class Registration(models.Model):
    """
    Links a participant to an event.
    Used for eligibility, opponent generation, and reports.
    """

    participant_name = models.CharField(max_length=100)
    house = models.CharField(max_length=50)

    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name='registrations'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('participant_name', 'event')

    def __str__(self):
        return f"{self.participant_name} - {self.event.name}"
