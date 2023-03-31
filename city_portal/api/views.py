from django.shortcuts import render
from django.http import HttpResponseNotFound


def base(request):
    return render(request, 'api/base.html')

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
