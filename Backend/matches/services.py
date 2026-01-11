# matches/services.py
"""
Match-related business logic.
"""

from .models import MatchOpponent

def advance_winner(match):
    """
    Marks winner and returns advancing participant.
    """
    winner = MatchOpponent.objects.filter(
        match=match,
        is_winner=True
    ).first()

    return winner.participant_name if winner else None
