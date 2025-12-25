from django.db import models

class Event(models.Model):
    SEVERITY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
        ('Critical', 'Critical'),
    ]
    EVENT_CHOICES = [
        ('intrusion', 'intrusion'),
        ('malware', 'malware'),
        ('anomaly', 'anomaly'),
    ]

    source_name = models.CharField(max_length=100)
    event_type = models.CharField(max_length=50, choices=EVENT_CHOICES)
    severity = models.CharField(max_length=10, choices=SEVERITY_CHOICES)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=['severity']),
            models.Index(fields=['timestamp']),
        ]

    def __str__(self):
        return f"{self.event_type} - {self.severity}"
