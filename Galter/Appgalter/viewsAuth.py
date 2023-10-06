
import json
from .forms import *
from typing import *
from .models import *
from datetime import *
from django.conf import *
from django.http import *
from django.views import *
from django.shortcuts import *
from django.contrib.auth import *
from django.contrib import messages
from django.utils.decorators import *
from django.views.decorators.csrf import *
from django.contrib.auth.decorators import * 


class RegistrarUsuarioView(View):
    template_name = 'registroUser.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
        form = UserForm(request.POST)  # Definir form con un valor predeterminado
        if request.method == 'POST':
            print("en el metodo")
            #if request.headers.get('content-type') == 'application/json':
            if 'application/json' in request.headers.get('content-type', ''):
                print("en el json")
                self.handle_flutter_data(request)
                print("EN FLUTTER")
            else:
                print("en django")
                form = UserForm(request.POST)
                if form.is_valid():
                    print("form valid")
                    if form.cleaned_data['imagen'] or form.cleaned_data['imagen'] is None:
                        print("is none")
                        form.save()
                        imagen_file = request.FILES['imagen']

                        user_instance = form.save(commit=False)
                        user_instance.imagen = imagen_file
                        user_instance.save()

                        messages.success(request, 'registrado desde html')
                        return redirect("iniciar_sesion")
                else:
                    print("EERRR", form.errors)
                    messages.error(request, 'Error al registrar el usuario desde formulario HTML.')
        else:
            print("no metodo")
            form = UserForm()
        return render(request, self.template_name, {'form': form})

    def get(self, request):
        form = UserForm()
        return render(request, self.template_name, {'form': form})

    def handle_flutter_data(self, request):
        try:
            data = json.loads(request.body)
            print("Datos recibidos desde Flutter:")
            print(data)  # Imprime los datos recibidos desde Flutter
            form = UserForm(data)
            if form.is_valid():
                print("Datos válidos:")
                print(form.cleaned_data)  # Imprime los datos validados por el formulario
                form.save()
                messages.success(request, 'Usuario registrado correctamente desde Flutter.')
            else:
                print("Errores en el formulario:")
                print(form.errors)  # Imprime los errores de validación del formulario
        except json.JSONDecodeError:
            messages.error(request, 'Error en los datos enviados desde Flutter.')

class IniciarSesionView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'iniciosesion.html', {'form':form})
    
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        if request.method.lower() == "get":
            return self.get(request, *args, **kwargs)
        elif request.method.lower() == "post":
            return self.post(request, *args, **kwargs)
    
    def post(self, request):
        accept_header = request.META.get('HTTP_ACCEPT', '')
        print("*********************")

        if 'application/json' in accept_header:
            print("en json")
            try:
                json_data = json.loads(request.body)
                username = json_data.get('username')
                password = json_data.get("password")
                user = authenticate(username = username, password = password)

                if user is not None:
                    print("json validation")
                    login(request, user)

                    if user.rol == 'admin':
                        response_data ={
                            'message' : 'Inicio de Sesion',
                            "user_id" : user.codigo_id,
                            "username" : user.username,
                            "rol" : user.rol,
                        }
                        return JsonResponse(response_data)
                    else:
                        return JsonResponse({'error': 'es empleado'}, status = 400)
                else:
                    return JsonResponse({'error' : 'Datos incorrectos'}, status = 400)
            
            except json.JSONDecodeError:
                return HttpResponseBadRequest('Invalid JSON data')
        else:
            form = LoginForm(data = request.POST)

            if form.is_valid():
                print("vvvvvvvvvvvvv")
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)

                if user is not None:
                    login(request, user)
                    if user.rol == "admin":
                        return redirect("menus")
                    else:
                        return JsonResponse({'message' : 'Inicio de sesion'})
                else:
                    return JsonResponse({'error' : 'Datos incorrectos'}, status = 400)
            else:
                return JsonResponse({'error' : 'Formularion incorrecto'}, status = 400)
                    


class PerfilUsuarioView(View):
    template_name = 'actUsuario.html'

    def generate_token(self, user):
        token_options = {
            'iat' : datetime.utcnow(),
            'exp' : datetime.utcnow() + timedelta(hours = 1),
            'user_id' : user.codigo_id,
        }
        token = jwt.encode(token_options, settings.SECRET_KEY, algorithm = 'HS256')
        return token
    
    @method_decorator(login_required(login_url='iniciar_sesion'))
    def get(self, request):
        try:
            user_ = User.objects.get(codigo_id=request.user.codigo_id)
            userr = request.user
            user_data = {
                'password': user_.password,
                'username': user_.username,
                'rol':user_.rol,
                'imagen':user_.imagen,
            }
            accept_header = request.META.get('HTTP_ACCEPT', '')

            if 'application/json' in accept_header:
                token = self.generate_token(request.user)
                return JsonResponse({'token':token, **user_data})
            else:
                form = UpdateUser(instance = userr)
                return render(request, self.template_name, {'form': form, 'user':userr})
        except User.DoesNotExist:
            return JsonResponse({'error' : 'No se encontraron datos del User'}, status = 400)


    @method_decorator(login_required(login_url='iniciar_sesion'))
    def post(self, request):
        try:
            user_ = User.objects.get(codigo_id=request.user.codigo_id)
        except User.DoesNotExist:
            messages.error(request, 'No se encontraron los datos del user.')
            return redirect('menus')

        form = UpdateUser(request.POST, instance=user_)

        if form.is_valid():
            print("form valid")
            form.save()
            messages.success(request, 'Cambios guardados')
            accept_header = request.META.get('HTTP_ACCEPT', '')

            if 'application/json' in accept_header:
                user_data = {
                    'password': user_.password,
                    'username': user_.username,
                    'rol':user_.rol,
                    'imagen':user_.imagen,
                }
                return JsonResponse(user_data)
            else:
                return redirect('update_usuario')
        return render(request, self.template_name, {'form': form, 'user': user_}) 

"""                 print("imagen en diccionario")
                imagen_file = request.FILES['imagen']
                user_instance = form.save(commit=False)
                user_instance.imagen = imagen_file
                user_instance.save()
                form.save()
                messages.success(request, 'Cambios guardados correctamente.')
                return redirect('update_usuario')
            else:
                messages.success(request, 'No se ha seleccionado una imgen')
        else:
            print("ERROR")
            messages.error(request,"Error al actualizar user")

        return render(request, self.template_name, {'form': form, 'user': userr}) """

def frmUpdateUser(request):
    return render(request, "actUsuario.html")

