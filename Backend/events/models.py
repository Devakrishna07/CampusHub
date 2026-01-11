from django.db import models
from accounts.models import User

# Create your models here.
class Venue(models.Model):
    name = models.CharField(max_length=255)
    location = models.TextField()

    def __str__(self):
        return self.name
    
class Event(models.Model):
    name = models.CharField(max_length=255)
    venue=models.ForeignKey(Venue, on_delete=models.CASCADE)
    coordinator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='coordinated_events')
    is_group_event = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
class RoundTemplate(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name