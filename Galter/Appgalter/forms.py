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
            'class':'controls',
            'placeholder':'Documento',  
            'maxlength':'10',
<<<<<<< HEAD
            'minlength':'1'
        })
        self.fields['username'].widget.attrs.update({
            'required':'',
            'name':'username_input',
            'id':'username_input',
            'type':'text',
            'class':'form-input',
            'placeholder':'Nombre de usuario',  
            'maxlength':'',
            'minlength':'1'
        })
=======
            'minlength':'1'
        })
        self.fields['username'].widget.attrs.update({
            'required':'',
            'name':'name_input',
            'id':'name_input',
            'type':'text',
            'class':'controls',
            'placeholder':'Nombre de Usuario',  
            'maxlength':'20',
            'minlength':'1'
        })
>>>>>>> 3ac4fa8dd02759d35568a58a20153c3b72a53286
        self.fields['email'].widget.attrs.update({
            'required':'',
            'name':'email_input',
            'id':'email_input',
<<<<<<< HEAD
            'type':'text',
            'class':'form-input',
            'placeholder':'Correo electronico',  
            'maxlength':'',
            'minlength':'1'
        })
        self.fields['password1'].widget.attrs.update({
            'required':'',
            'name':'password1_input',
            'id':'password1_input',
            'type':'password',
            'class':'form-input',
            'placeholder':'Contraseña',  
            'maxlength':'',
            'minlength':'1'
        })
        self.fields['password2'].widget.attrs.update({
            'required':'',
            'name':'password2_input',
            'id':'password2_input',
            'type':'password',
            'class':'form-input',
            'placeholder':'Confirme la contraseña',  
            'maxlength':'',
            'minlength':'1'
=======
            'type':'email',
            'class':'controls',
            'placeholder':'Correo Electronico',  
        })
        self.fields['password1'].widget.attrs.update({
            'required':'',
            'name':'pass1_input',
            'id':'pass1_input',
            'type':'password',
            'class':'controls',
            'placeholder':'Contraseña',  
        })
        self.fields['password2'].widget.attrs.update({
            'required':'',
            'name':'pass2_input',
            'id':'pass2_input',
            'type':'password',
            'class':'controls',
            'placeholder':'Confirmar Contraseña',  
>>>>>>> 3ac4fa8dd02759d35568a58a20153c3b72a53286
        })
        self.fields['rol'].widget.attrs.update({
            'required':'',
            'name':'rol_input',
            'id':'rol_input',
            'type':'text',
<<<<<<< HEAD
            'class':'form-input',
            'placeholder':'Rol',  
            'maxlength':'',
            'minlength':'1'
        })
        self.fields['imagen'].widget.attrs.update({
            'id':'imagen_input',
            'type':'file',
            'class':'form-input',
        })
        

=======
            'class':'controls',
            'placeholder':'Rod de Usuario',  
        })
        self.fields['imagen'].widget.attrs.update({
            'name':'img',
            'id':'img',
            'type':'file',
            'class':'controls'
        })
>>>>>>> 3ac4fa8dd02759d35568a58a20153c3b72a53286
    rol = forms.CharField(max_length=100)
    imagen = forms.ImageField(required=False)
    codigo = forms.CharField(max_length=10)

    class Meta:
        model = User
        fields = ['codigo','username','email','password1','password2','rol','imagen']



class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'required':'',
            'name':'usuario',
            'id':'usuario',
            'type':'text',
            'class':'controls',
            'placeholder':'Nombre de Usuario',  
            'minlength':'1'
        })
        self.fields['password'].widget.attrs.update({
            'required':'',
            'name':'contrasena',
            'id':'contrasena',
            'type':'password',
            'class':'controls',
            'placeholder':'Contraseña',  
            'minlength':'1'
        })
    username = forms.CharField()
    password = forms.CharField()
    class Meta:
        model : User
        fields = {'username','password'}


class UpdateUser(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['imagen'].widget.attrs.update({
            'name':'img',
            'id':'img',
            'type':'file',
            'class':'controls'
        })
    class Meta:
        model = User
        fields = ['username','email','rol','imagen','password']