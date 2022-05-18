from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, get_object_or_404
from django.core.files.storage import FileSystemStorage

from .models import Sensor, Measurement
from .serializers import SensorSerializer, SensorDetailSerializer, MeasurementSerializer


class MeasurementView(ListCreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    def perform_create(self, serializer):
        sensor = get_object_or_404(Sensor, id=self.request.data.get('id_sensor'))
        if self.request.FILES:
            file = self.request.FILES['file']
            fs = FileSystemStorage()
            file_name = fs.save(file.name, file)
            file_url = fs.url(file_name)
        return serializer.save(id_sensor=sensor, image=file_url)


class SensorViewSet(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class SensorDetailView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer
