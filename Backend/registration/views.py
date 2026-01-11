# registration/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Registration
from .serializers import RegistrationSerializer
from core.permissions import IsAdmin

class PublicRegistrationView(APIView):
    """
    Public endpoint to register for an event.
    No authentication required.
    """

    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {"message": "Registration successful"},
            status=201
        )


class EventParticipantsView(APIView):
    """
    View participants of an event.
    Accessible to authorized roles only.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, event_id):
        registrations = Registration.objects.filter(event_id=event_id)
        serializer = RegistrationSerializer(registrations, many=True)
        return Response(serializer.data)
