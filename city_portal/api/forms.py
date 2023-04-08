from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


class RegisterUserForm(UserCreationForm):
    patronymic = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Отчество'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Пароль'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Повторите пароль'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'patronymic', 'username', 'email', 'password1', 'password2')

        widgets = {
            'first_name': forms.TextInput(attrs={
                'placeholder': 'Имя'
            }),
            'last_name': forms.TextInput(attrs={
                'placeholder': 'Фамилия'
            }),
            'username': forms.TextInput(attrs={
                'placeholder': 'Логин'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Электронная почта'
            }),
        }


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'placeholder': 'Логин'}))
    password = forms.CharField(max_length=16, widget=forms.PasswordInput(attrs={'placeholder': 'Пароль'}))
