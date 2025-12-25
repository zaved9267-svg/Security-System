from rest_framework import generics
from .models import Event
from .serializers import EventSerializer
from .permissions import IsAdmin

class EventCreateAPIView(generics.CreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAdmin]
