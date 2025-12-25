from rest_framework import serializers
from .models import Alert

class AlertSerializer(serializers.ModelSerializer):
    event = serializers.StringRelatedField()

    class Meta:
        model = Alert
        fields = ['id', 'event', 'status', 'created_at']
        read_only_fields = ['created_at']
