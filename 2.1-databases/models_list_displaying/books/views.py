from django.shortcuts import render, redirect
from books.models import Book
from django.http import HttpResponse


def index(request):
    return redirect('books')


def books_view(request, date=None):
    books = Book.objects.all()
    prev_page = None
    next_page = None
    error404 = False
    if date:
        date = date.date()
        date_list = [b.pub_date for b in books]
        if date in date_list:
            date_list.sort()
            date_index = date_list.index(date)
            if date_index - 1 >= 0:
                prev_page = date_list[date_index - 1]
            if date_index + 1 < len(date_list):
                next_page = date_list[date_index + 1]
            books = Book.objects.filter(pub_date=date)
        else:
            error404 = True
    template = 'books/books_list.html'
    context = {
        'books': books,
        'prev_page': prev_page,
        'next_page': next_page
    }
    if error404:
        result = HttpResponse('Страница не найдена')
    else:
        result = render(request, template, context)
    return result
