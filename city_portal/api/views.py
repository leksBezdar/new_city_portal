from django.contrib.auth import logout
import re
from django.contrib.auth.views import LoginView
from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import RegisterUserForm, LoginUserForm


def profile(request):
    return render(request, "api/profile.html")

def application(request):
    return render(request, "api/application.html")


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'api/login.html'

    def get_success_url(self):
        return reverse_lazy('profile')


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'api/registr.html'
    success_url = reverse_lazy('login')

    # def clean(self):
    #     fio_pattern = re.compile(r'^[?!,.а-яА-ЯёЁ0-9\s]+$')
    #     data_f = self.cleaned_data['first_name']
    #     data_i = self.cleaned_data['first_name']
    #     data_o = self.cleaned_data['first_name']
    #     if self.
    #     return redirect('login')


def logout_user(request):
    logout(request)
    return redirect('login')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
