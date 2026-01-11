# matches/admin.py
from django.contrib import admin
from .models import Match, MatchOpponent

admin.site.register(Match)
admin.site.register(MatchOpponent)
