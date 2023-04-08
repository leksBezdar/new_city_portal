from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm


def regist(request):
    data = {}
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            data['form'] = form
            data['res'] = "Всё прошло успешно"
        return render(request, 'api/registr.html', data)
    else:
        form = RegisterUserForm()
        data['form'] = form
    return render(request, 'api/registr.html', data)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
