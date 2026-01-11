# events/urls.py
from django.urls import path
from .views import (
    EventListView,
    EventCreateView,
    VenueView,
    RoundTemplateView
)

urlpatterns = [
    path('events/', EventListView.as_view()),
    path('events/create/', EventCreateView.as_view()),
    path('venues/', VenueView.as_view()),
    path('round-templates/', RoundTemplateView.as_view()),
]
