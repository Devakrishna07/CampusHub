# scoring/urls.py
from django.urls import path
from .views import SubmitScoreView, MatchScoreView

urlpatterns = [
    path('submit/', SubmitScoreView.as_view()),
    path('match/<int:match_id>/', MatchScoreView.as_view()),
]
