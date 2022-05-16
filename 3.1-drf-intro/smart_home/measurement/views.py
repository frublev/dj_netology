# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django.core.files.storage import FileSystemStorage
from rest_framework.decorators import action

from .models import Sensor, Measurement
from .serializers import SensorDetailSerializer, MeasurementSerializer


class MeasurementView(APIView):
    def get(self, request):
        measurement = Measurement.objects.all()
        serial = MeasurementSerializer(measurement, many=True)
        return Response(serial.data)

    def post(self, request):
        req = request.data
        sensor = Sensor.objects.get(pk=req['sensor'])
        if request.FILES:
            file = request.FILES['file']
            fs = FileSystemStorage()
            filename = fs.save(file.name, file)
            file_url = fs.url(filename)
            sensor.measurements.create(temperature=req['temperature'], image=file_url)
        else:
            sensor.measurements.create(temperature=req['temperature'])
        return Response({'status': 'OK'})


class SensorViewSet(ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

