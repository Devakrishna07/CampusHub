# scoring/services.py
"""
Scoring-related business logic.
"""

from .models import Score
from matches.models import MatchOpponent

def calculate_winner(match):
    """
    Determines the winner of a match based on scores.
    Marks the winner in MatchOpponent.
    """

    scores = Score.objects.filter(match=match)

    if not scores.exists():
        return None

    winner_score = max(scores, key=lambda s: s.points)

    MatchOpponent.objects.filter(
        match=match
    ).update(is_winner=False)

    MatchOpponent.objects.filter(
        match=match,
        participant_name=winner_score.participant_name
    ).update(is_winner=True)

    match.is_completed = True
    match.save()

    return winner_score.participant_name
