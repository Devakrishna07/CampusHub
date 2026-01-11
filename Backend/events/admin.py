# events/admin.py
from django.contrib import admin
from .models import Event, Venue, RoundTemplate

admin.site.register(Event)
admin.site.register(Venue)
admin.site.register(RoundTemplate)
