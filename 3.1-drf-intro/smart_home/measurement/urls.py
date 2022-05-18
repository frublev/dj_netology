from django.urls import path
from .views import SensorViewSet, MeasurementView, SensorDetailView


urlpatterns = [
    path('measurements/', MeasurementView.as_view()),
    path('sensors/', SensorViewSet.as_view()),
    path('sensors/<pk>/', SensorDetailView.as_view()),
]
