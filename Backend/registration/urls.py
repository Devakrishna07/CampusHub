# registration/urls.py
from django.urls import path
from .views import PublicRegistrationView, EventParticipantsView

urlpatterns = [
    path('register/', PublicRegistrationView.as_view()),
    path('event/<int:event_id>/participants/', EventParticipantsView.as_view()),
]
