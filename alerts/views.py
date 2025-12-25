from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from rest_framework import generics
from .models import Alert
from .serializers import AlertSerializer
from .permissions import IsAdmin, IsAdminOrReadOnly, AnalystReadOnly

class AlertListAPIView(generics.ListAPIView):
    serializer_class = AlertSerializer
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        queryset = Alert.objects.select_related("event")

        severity = self.request.query_params.get("severity")
        status = self.request.query_params.get("status")

        if severity:
            queryset = queryset.filter(event__severity=severity)
        if status:
            queryset = queryset.filter(status=status)

        return queryset.order_by("-created_at")


class AlertUpdateAPIView(generics.UpdateAPIView):
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer
    permission_classes = [IsAdmin]

class AlertViewSet(ModelViewSet):
    queryset = Alert.objects.select_related('event')  # avoids N+1 queries
    serializer_class = AlertSerializer
    permission_classes = [IsAuthenticated, AnalystReadOnly]