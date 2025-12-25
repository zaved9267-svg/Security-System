from rest_framework import serializers
from .models import Event
from alerts.models import Alert

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'
        read_only_fields = ['timestamp']

    def create(self, validated_data):
        event = Event.objects.create(**validated_data)

        if event.severity in ['High', 'Critical']:
            Alert.objects.create(event=event)

        return event
