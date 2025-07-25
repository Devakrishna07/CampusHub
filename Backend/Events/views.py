from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly, IsAdminUser
from .models import EventPoster
from .serializers import EventSerializer

# Create your views here.
class PublicEventsView(generics.ListAPIView):
    queryset = EventPoster.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class EventRetrieveView(generics.RetrieveAPIView):
    queryset = EventPoster.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class EventCreateView(generics.ListCreateAPIView):
    generics = EventPoster.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAdminUser]

class EventEditView(generics.RetrieveUpdateDestroyAPIView):
    generics = EventPoster.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAdminUser]


