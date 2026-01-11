# scoring/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Score
from .serializers import ScoreSerializer
from .services import calculate_winner
from core.permissions import IsAdmin

class SubmitScoreView(APIView):
    """
    Judges submit scores for a match.
    """
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ScoreSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        score = serializer.save()

        calculate_winner(score.match)

        return Response(
            {"message": "Score submitted successfully"},
            status=201
        )


class MatchScoreView(APIView):
    """
    View scores of a specific match.
    Publicly accessible.
    """

    def get(self, request, match_id):
        scores = Score.objects.filter(match_id=match_id)
        serializer = ScoreSerializer(scores, many=True)
        return Response(serializer.data)
