import datetime
import os
from django.conf import settings
from django.shortcuts import render


def file_list(request, date=None):
    template_name = 'index.html'
    files = []
    
    # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:
    file_list1 = os.listdir(settings.FILES_PATH)
    for file in file_list1:
        ctime = datetime.datetime.fromtimestamp(os.path.getctime(settings.FILES_PATH+f'/{file}'))
        mtime = datetime.datetime.fromtimestamp(os.path.getmtime(settings.FILES_PATH + f'/{file}'))
        print(ctime, mtime)
        if date:
            date1 = date.date()
        else:
            date1 = None
        if ctime.date() == date1 or mtime.date() == date1 or date is None:
            files.append({
                'name': file,
                'ctime': ctime,
                'mtime': mtime
            })

    context = {
        'files': files,
        'date': date
    }

    return render(request, template_name, context)


def file_content(request, name):
    # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:
    with open(settings.FILES_PATH+f'/{name}') as report_file:
        content = report_file.read()
    return render(
        request,
        'file_content.html',
        context={'file_name': name, 'file_content': content}
    )
