import json

from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.http import HttpResponseNotFound, HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView

from .forms import RegisterUserForm, LoginUserForm
from django.views.decorators.cache import cache_control


def profile(request):
    return render(request, "api/profile.html")


def application(request):
    return render(request, "api/application.html")


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'api/login_or_reg.html'

    def get_success_url(self):
        return reverse_lazy('profile')


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'api/login_or_reg.html'
    success_url = reverse_lazy('profile')


def login_or_reg(request, *args, **kwargs):
    if 'password2' in request.POST:
        return RegisterUser.as_view()
    return LoginUser.as_view()


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def logout_user(request):
    logout(request)
    return redirect('home')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
