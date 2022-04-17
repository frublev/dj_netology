from django.shortcuts import render

from articles.models import Article


def articles_list(request):
    template = 'articles/news.html'
    object_list = Article.objects.all()
    print(object_list)
    context = {'object_list': object_list}

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/3.1/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = '-published_at'

    return render(request, template, context)
