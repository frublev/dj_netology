from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
import csv


bus_stations_list = []


def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request):
    with open(settings.BUS_STATION_CSV, encoding='utf-8') as csv_file:
        bus_stations_csv = csv.DictReader(csv_file)
        for bs in bus_stations_csv:
            bus_stations_list.append(bs)
    page_number = request.GET.get('page')
    if page_number:
        try:
            current_page = int(page_number)
        except ValueError:
            current_page = 1
    else:
        current_page = 1
    paginator = Paginator(bus_stations_list, 10)
    page = paginator.get_page(current_page)
    return render(request, 'stations/index.html', context={
        'bus_stations': page
    })
