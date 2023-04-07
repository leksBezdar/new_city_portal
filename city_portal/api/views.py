from django.contrib.auth.views import LoginView
from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import *
from .models import *


def base(request):
    return render(request, 'api/register_and_login.html')


# class LoginUser(LoginView):
#     form_class = LoginUserForm
#     template_name = 'api/register_and_login.html'


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'api/register_and_login.html'
    success_url = reverse_lazy('home')


# def login_or_reg(request, *args, **kwargs):
#     if 'password2' in request.POST:
#         return RegisterUser.as_view()(request)  # Не уверен, нужно ли передавать args и kwargs
#     return LoginUser.as_view()(request)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
