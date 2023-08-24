from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import *
from .models import *

User = get_user_model()

class UserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['codigo'].widget.attrs.update({
            'required':'',
            'name':'codigo_input',
            'id':'codigo_input',
            'type':'text',
            'class':'form-input',
            'placeholder':'Documento',  
            'maxlength':'20',
            'minlength':'1'
        })
        """ rol = forms.CharField(max_length=100)
        imagen = forms.ImageField(required=False)
        codigo = forms.CharField(max_length=10) """
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