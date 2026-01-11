# matches/urls.py
from django.urls import path
from .views import (
    MatchListView,
    AutoMatchCreateView,
    ManualMatchCreateView
)

urlpatterns = [
    path('event/<int:event_id>/', MatchListView.as_view()),
    path('auto/<int:event_id>/', AutoMatchCreateView.as_view()),
    path('manual/', ManualMatchCreateView.as_view()),
]
