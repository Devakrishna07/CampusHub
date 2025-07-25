from django.db import models

# Create your models here.
class EventPoster(models.Model):
    EventTitle = models.CharField(max_length=200)
    EventDate = models.DateField()
    EventTime = models.TimeField()
    Venue = models.TextField()
    Organizer = models.CharField(max_length=200)
    Contact = models.CharField(max_length=200)
    Organizer2 = models.CharField(max_length=200, null=True)
    Contact2 = models.CharField(max_length=100, null=True)
    poster_image = models.URLField()
    Description = models.TextField()

    #optional Fields
    Entry_details = models.TextField(blank=True, null=True)
    HighLights = models.TextField(blank=True, null=True)
    Registration_link = models.URLField(blank=True, null=True)
    Sponsors = models.TextField(blank=True, null=True)
    
    #social media links
    Instagram_link = models.URLField(blank=True, null=True)
    FaceBook = models.URLField(blank=True, null=True)
    Whatsapp = models.URLField(blank=True, null=True)
    Website = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.EventTitle