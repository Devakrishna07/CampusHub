from django.contrib.auth.models import AbstractUser
from django.db import models
from core.constants import USER_ROLES

class User(AbstractUser):
    """
    Custom user model with role-based access control.
    """

    role = models.CharField(
        max_length=20,
        choices=USER_ROLES
    )

    authorized_events = models.ManyToManyField(
        'events.Event',
        blank=True,
        related_name='authorized_users'
    )

    def __str__(self):
        return f"{self.username} ({self.role})"                    