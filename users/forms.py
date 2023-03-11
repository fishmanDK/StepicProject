from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from users.models import *
from django import forms
class UserLoginForm(AuthenticationForm):

    class Meta:
        model = User
        fields = ('username', 'password')


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control py-4",
        "placeholder": "Введите имя",
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control py-4",
        "placeholder": "Введите фамилию",
    }))
    user_name = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control py-4",
        "placeholder": "Введите имя пользователя",
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        "class": "form-control py-4",
        "placeholder": "Введите адрес эл. почты",
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "form-control py-4",
        "placeholder": "Введите пароль",
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "form-control py-4",
        "placeholder": "Подтвердите пароль",
    }))
    class Meta:
        model = User
        fields = ('first_name', 'last_name', "user_name", 'email', 'password1', 'password2')