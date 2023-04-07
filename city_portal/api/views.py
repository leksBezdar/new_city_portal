from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

from .models import *
from .forms import *


def registration(request):
    error = ''
    if request.method == "POST":
        form = CreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('')
        else:
            error = "Одно или несколько полей были заполнены неверно"

    form = CreationForm
    log_form = LoginForm
    data = {
        'form': form,
        'log_form': log_form,
        'error': error
    }
    return render(request, 'api/signup.html', data)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
