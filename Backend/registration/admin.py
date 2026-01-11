# registration/admin.py
from django.contrib import admin
from .models import Registration

@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('participant_name', 'house', 'event')
    list_filter = ('house', 'event')
