from collections import Counter

from django.shortcuts import render

# Для отладки механизма ab-тестирования используйте эти счетчики
# в качестве хранилища количества показов и количества переходов.
# но помните, что в реальных проектах так не стоит делать
# так как при перезапуске приложения они обнулятся
counter_show = Counter()
counter_click = Counter()


def index(request):
    # Реализуйте логику подсчета количества переходов с лендига по GET параметру from-landing
    page = request.GET.get('from-landing')
    if page == 'original':
        counter_click['original'] += 1
    elif page == 'test':
        counter_click['test'] += 1
    else:
        pass
    return render(request, 'index.html')


def landing(request):
    page = request.GET.get('ab-test-arg')
    if page == 'original':
        temp = 'landing.html'
        counter_show['original'] += 1
    elif page == 'test':
        temp = 'landing_alternate.html'
        counter_show['test'] += 1
    else:
        temp = None
    # Реализуйте дополнительное отображение по шаблону app/landing_alternate.html
    # в зависимости от GET параметра ab-test-arg
    # который может принимать значения original и test
    # Так же реализуйте логику подсчета количества показов
    return render(request, temp)


def stats(request):
    # Реализуйте логику подсчета отношения количества переходов к количеству показов страницы
    # Для вывода результат передайте в следующем формате:
    test_conversion = counter_click['test'] / counter_show['test']
    original_conversion = counter_click['original'] / counter_show['original']
    return render(request, 'stats.html', context={
        'test_conversion': test_conversion,
        'original_conversion': original_conversion,
    })
