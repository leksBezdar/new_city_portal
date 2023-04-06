from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from django.forms import TextInput, EmailInput, PasswordInput, CharField


User = get_user_model()


class CreationForm(UserCreationForm):
    password1 = CharField(max_length=16, widget=PasswordInput(attrs={'placeholder': 'Пароль'}),)
    password2 = CharField(max_length=16, widget=PasswordInput(attrs={'placeholder': 'Повторите пароль'}))
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')

        widgets = {
            'first_name': TextInput(attrs={
                'placeholder': 'Имя'
            }),
            'last_name': TextInput(attrs={
                'placeholder': 'Фамилия'
            }),
            'username': TextInput(attrs={
                'placeholder': 'Логин'
            }),
            'email': EmailInput(attrs={
                'placeholder': 'Электронная почта'
            }),
        }

class CreationForm(UserCreationForm):
    password1 = CharField(max_length=16, widget=PasswordInput(attrs={'placeholder': 'Пароль'}),)
    password2 = CharField(max_length=16, widget=PasswordInput(attrs={'placeholder': 'Повторите пароль'}))
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')

        widgets = {
            'first_name': TextInput(attrs={
                'placeholder': 'Имя'
            }),
            'last_name': TextInput(attrs={
                'placeholder': 'Фамилия'
            }),
            'username': TextInput(attrs={
                'placeholder': 'Логин'
            }),
            'email': EmailInput(attrs={
                'placeholder': 'Электронная почта'
            }),
        }
