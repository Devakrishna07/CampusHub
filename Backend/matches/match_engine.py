# matches/match_engine.py
import random
from .models import Match, MatchOpponent

def auto_generate_matches(event, participants, round_name):
    """
    Automatically pairs participants and creates matches.
    """
    random.shuffle(participants)

    matches = []
    for i in range(0, len(participants), 2):
        match = Match.objects.create(
            event=event,
            round_name=round_name,
            start_time=None,
            venue=event.venue.name
        )

        MatchOpponent.objects.create(
            match=match,
            participant_name=participants[i]
        )

        if i + 1 < len(participants):
            MatchOpponent.objects.create(
                match=match,
                participant_name=participants[i + 1]
            )

        matches.append(match)

    return matches
