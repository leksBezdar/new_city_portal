from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from .forms import RegisterUserForm
from django.contrib.auth import login as auth_login


def home(request):
    return render(request, "api/base.html")

def regist(request):
    data = {}
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            data['form'] = form
            data['res'] = "Всё прошло успешно"
            return redirect("login")
        return render(request, 'api/registr.html', data)
    else:
        form = RegisterUserForm()
        data['form'] = form
    return render(request, 'api/registr.html', data)


def login(request):
    context = {}
    if request.method == "POST":
        form = AuthenticationForm(request.POST)

        if form.is_valid:  # returns True
            name = request.POST["username"]
            pswd = request.POST["password"]
            user = authenticate(request, username=name, password=pswd)
            print("user = " + str(user))  # always returns None

            if user:
                print("valid user " + str(user))
                auth_login(request, user)
                print("user is " + str(request.user.is_authenticated))
                return redirect("home")
    form = AuthenticationForm()
    context['login_form'] = form
    return render(request, 'api/login.html', context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
