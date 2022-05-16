from django.urls import path
from .views import SensorViewSet, MeasurementView

from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('sensors', SensorViewSet)

urlpatterns = [
    path('measurements/', MeasurementView.as_view()),
    # path('weapon/<pk>/', WeaponView.as_view()),
    # TODO: зарегистрируйте необходимые маршруты
] + router.urls
