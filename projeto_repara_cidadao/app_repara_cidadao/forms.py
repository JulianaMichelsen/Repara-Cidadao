from django import forms
from .models import Reparo
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class ReparoModelForm(forms.ModelForm):

    class Meta:
        model = Reparo
        fields = ['reparo', 'rua', 'numero', 'complemento', 'bairro', 'cidade', 'estado', 'cep', 'referencia', 'imagem']

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", 'email', 'password1', 'password2']

