# scoring/admin.py
from django.contrib import admin
from .models import Score

@admin.register(Score)
class ScoreAdmin(admin.ModelAdmin):
    list_display = ('participant_name', 'points', 'match')
    list_filter = ('match',)
    search_fields = ('participant_name',)