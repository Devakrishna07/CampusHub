# matches/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Match, MatchOpponent
from .serializers import MatchSerializer
from .match_engine import auto_generate_matches
from core.permissions import IsAdmin

class MatchListView(APIView):
    """
    Public match schedule view.
    """
    def get(self, request, event_id):
        matches = Match.objects.filter(event_id=event_id)
        return Response(MatchSerializer(matches, many=True).data)


class AutoMatchCreateView(APIView):
    """
    Coordinator/Admin auto-match generation.
    """
    permission_classes = [IsAuthenticated, IsAdmin]

    def post(self, request, event_id):
        participants = request.data.get('participants')
        round_name = request.data.get('round_name')

        matches = auto_generate_matches(
            event_id,
            participants,
            round_name
        )

        return Response(
            MatchSerializer(matches, many=True).data,
            status=201
        )


class ManualMatchCreateView(APIView):
    """
    Manual match creation by coordinator.
    """
    permission_classes = [IsAuthenticated]

    def post(self, request):
        match = Match.objects.create(
            event_id=request.data['event'],
            round_name=request.data['round_name'],
            start_time=request.data['start_time'],
            venue=request.data['venue']
        )

        for p in request.data['participants']:
            MatchOpponent.objects.create(
                match=match,
                participant_name=p
            )

        return Response(
            MatchSerializer(match).data,
            status=201
        )
