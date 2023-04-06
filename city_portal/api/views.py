from django.http import HttpResponseNotFound
from django.shortcuts import render

from .models import *


def base(request):
    return render(request, 'api/base.html')

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
