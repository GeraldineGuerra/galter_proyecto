from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import *
from .models import *

User = get_user_model()

class UserForm(UserCreationForm):
    rol = forms.CharField(max_length=100)
    imagen = forms.ImageField(required=False)
    codigo = forms.CharField(max_length=10)

    class Meta:
        model = User
        fields = ['codigo','username','email','password1','password2','rol','imagen']


class LoginForm(AuthenticationForm):
    class Meta:
        model : User
        fields = {'username','password'}


class UpdateUser(forms.ModelForm):
    class Meta:
        model = usuario
        fields = ['nombre_usuario','correo_usuario']