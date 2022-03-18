from django.http import HttpResponse
from django.shortcuts import render, reverse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:


def index(request):
    pages = {}
    data_keys = list(DATA.keys())
    for k in data_keys:
        recipe_url = {k: f'/{k}'}
        pages.update(recipe_url)
    context = {'pages': pages}
    return render(request, 'calculator/menu.html', context)


def get_recipe(request, menu):
    count = request.GET.get('servings')
    if count:
        try:
            count = int(count)
        except ValueError or TypeError:
            print('Значение servings должно быть типа integer')
            count = 1
    else:
        count = 1
    recipe = DATA[menu].copy()
    for ingredient in recipe.keys():
        recipe[ingredient] = recipe[ingredient] * count
    context = {
        'recipe': recipe
    }
    return render(request, 'calculator/index.html', context)
