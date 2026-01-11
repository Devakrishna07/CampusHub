# registration/services.py
"""
Registration-related business rules.
"""

from .models import Registration

def get_event_participants(event):
    """
    Returns list of participants for an event.
    Used by coordinators and volunteers.
    """
    return Registration.objects.filter(event=event)
