from django.urls import path
from .views import AlertListAPIView, AlertUpdateAPIView

urlpatterns = [
    path('alerts/', AlertListAPIView.as_view(), name='list-alerts'),
    path('alerts/<int:pk>/', AlertUpdateAPIView.as_view(), name='update-alert'),
]
