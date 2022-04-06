from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    phones = Phone.objects.all()
    sort_ = request.GET.get('sort')
    if sort_ == 'name':
        phones = sorted(phones, key=lambda p: p.name)
    elif sort_ == 'min_price':
        phones = sorted(phones, key=lambda p: p.price)
    elif sort_ == 'min_price':
        phones = sorted(phones, key=lambda p: p.price, reverse=True)
    template = 'catalog.html'
    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    phone = Phone.objects.get(slug=slug)
    template = 'product.html'
    context = {'phone': phone}
    return render(request, template, context)
