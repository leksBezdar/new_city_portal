from django.http import HttpResponseNotFound
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import *
from .forms import *


def registration(request):
    error = ''
    if request.method == "POST":
        form = CreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home')
        else:
            error = "Одно или несколько полей были заполнены неверно"

    form = CreationForm
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'api/signup.html', data)

@login_required
def users(request):
    return render(
        request,
        'api/signup.html',
        {'all_users': User.objects.all()})

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
