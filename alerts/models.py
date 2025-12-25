from django.db import models
from events.models import Event

class Alert(models.Model):
    STATUS_CHOICES = [
        ('Open', 'Open'),
        ('Acknowledged', 'Acknowledged'),
        ('Resolved', 'Resolved'),
    ]

    event = models.OneToOneField(
        Event,
        on_delete=models.CASCADE,
        related_name='alert'
    )
    status = models.CharField(
        max_length=15,
        choices=STATUS_CHOICES,
        default='Open'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=['status']),
        ]

    def __str__(self):
        return f"Alert {self.id} - {self.status}"
