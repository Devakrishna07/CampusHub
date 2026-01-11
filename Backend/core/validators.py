# core/validators.py
"""
Validators for business rules.
Used in services and model clean() methods.
"""

from matches.models import Match

def validate_venue_clash(venue, start_time):
    """
    Prevents two matches at the same venue and time.
    Requirement: Avoid event clashes.
    """
    if Match.objects.filter(venue=venue, start_time=start_time).exists():
        raise ValueError("Venue already booked at this time.")


def validate_participant_clash(participant, start_time):
    """
    Prevents a participant from playing multiple matches at the same time.
    """
    if Match.objects.filter(
        matchopponent__participant=participant,
        start_time=start_time
    ).exists():
        raise ValueError("Participant has another match at this time.")
