from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    phones = Phone.objects.all()
    sort_ = request.GET.get('sort')
    if sort_ == 'name':
        phones = sorted(phones, key=lambda d: d.name)
    elif sort_ == 'min_price':
        phones = sorted(phones, key=lambda d: d.price)
    elif sort_ == 'min_price':
        phones = sorted(phones, key=lambda d: d.price, reverse=True)
    template = 'catalog.html'
    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    phone = Phone.objects.get(slug=slug)
    template = 'product.html'
    context = {'phone': phone}
    return render(request, template, context)
