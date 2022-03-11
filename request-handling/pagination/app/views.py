from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
import urllib.parse
import csv


bus_stations_list = []


def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request):
    with open(settings.BUS_STATION_CSV) as csv_file:
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
    if page.has_next():
        get_query = {'page': current_page + 1}
        params = urllib.parse.urlencode(get_query)
        next_page_url = f'{reverse("bus_stations")}?{params}'
    else:
        next_page_url = None
    if page.has_previous():
        get_query = {'page': current_page - 1}
        params = urllib.parse.urlencode(get_query)
        prev_page_url = f'{reverse("bus_stations")}?{params}'
    else:
        prev_page_url = None
    return render(request, 'index.html', context={
        'bus_stations': page,
        'current_page': current_page,
        'prev_page_url': prev_page_url,
        'next_page_url': next_page_url,
    })
