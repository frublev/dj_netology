from django.db import models


class Sensor(models.Model):

    name = models.CharField(max_length=256, verbose_name='Название')
    description = models.CharField(max_length=256, blank=True, verbose_name='Описание')


class Measurement(models.Model):

    id_sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    temperature = models.FloatField(verbose_name='Температура')
    created_at = models.DateField(auto_now_add=True, verbose_name='Дата измерения')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение')
