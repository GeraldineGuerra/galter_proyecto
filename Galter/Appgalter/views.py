import json
from typing import Any
from django.http import JsonResponse
from django.shortcuts import render


from Appgalter.models import usuario
from Appgalter.models import proveedor
from Appgalter.models import cliente, material, pedido, producto

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from django.views.generic import ListView,View





# def principal (request):
#     listarUsuarios=usuario.objects.all()
#     return render(request,"index1.html",{'usu': listarUsuarios})



# class listarUsuarios(ListView):
#     model=usuario
#     template_name="index1.html"

    


# class listarProveedor(ListView):
#     model=proveedor
#     template_name="index2.html"




# class listarCliente(ListView):
#     model=cliente
#     template_name="index3.html"



# class listarMaterial(ListView):
#     model=material
#     template_name="index4.html"




# class listarProducto(ListView):
#     model=producto
#     template_name="index5.html"



# class listarPedido(ListView):
#     model=pedido
#     template_name="index6.html"






# class listarUsuarios(View):
#     def get(self,request):
#         datos=usuario.objects.all().values()
#         datosusu=list(datos)
#         return render(request, 'index1.html',{'datos': datosusu})
        
#         #return JsonResponse(datosusu, safe=False)
    




class listarUsuarios(ListView):
    def get(self,request):
        datos=usuario.objects.all()
        datos_Usuarios=[]
        for i in datos:
            datos_Usuarios.append({ 
                'codi_usuario':i.codi_usuario,
                'nombre_usuario':i.nombre_usuario,
                'correo_usuario':i.correo_usuario,
                'pass_usuario':i.pass_usuario,
                'tipo_usuario':i.tipo_usuario
            }) 
        #datoscli=list(datos)
        return JsonResponse(datos_Usuarios, safe=False)
        #return render(request, 'index.html',{'datos': datoscli})
    

class InsertarUsuario(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    def post(self, request):
        try:
            datos=json.loads(request.body)
        except(json.JSONDecodeError,UnicodeDecodeError):
            return JsonResponse({"error": "Erra en la decodificacion"})
        codi_usuario = datos.get('codi_usuario')
        nombre_usuario = datos.get('nombre_usuario')
        correo_usuario = datos.get('correo_usuario')
        pass_usuario = datos.get('pass_usuario')
        tipo_usuario = datos.get('tipo_usuario')
        print(datos.get('codigo'))
        #cli=Cliente.objects.create(codi_usuario=datos['codi_usuario'],nombre_usuario=datos['nombre_usuario'],correo_usuario=datos['correo_usuario'],pass_usuraio=datos['pass_usuraio'],tipo_usuraio=datos['tipo_usuraio'])
        #cli.save()
        #return JsonResponse({'mensaje': 'datos guardados'})
        usu=usuario.objects.create(codi_usuario=codi_usuario, nombre_usuario=nombre_usuario, correo_usuario=correo_usuario, pass_usuario=pass_usuario, tipo_usuario=tipo_usuario)
        usu.save()
        
        return JsonResponse({'mensaje': 'datos guardados'})
        # return render(request,'insertarCli.html',{'mensaje': 'Datos guardados'})


def formularioInsertar(request):
    return render(request,"insertarUsu.html")    








class listarClientes(ListView):
    def get(self,request):
        datos=cliente.objects.all()
        datos_clientes=[]
        for i in datos:
            datos_clientes.append({ 
                'id_cliente':i.id_cliente,
                'nombre_cliente':i.nombre_cliente,
                'telefono_cliente':i.telefono_cliente,
                'representante_cliente':i.representante_cliente,
                'direccion':i.direccion
            }) 
        return JsonResponse(datos_clientes, safe=False)
        

class InsertarCliente(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    def post(self, request):
        try:
            datos=json.loads(request.body)
        except(json.JSONDecodeError,UnicodeDecodeError):
            return JsonResponse({"error": "Error en la decodificacion"})
        id_cliente = datos.get('id_cliente')
        nombre_cliente = datos.get('nombre_cliente')
        telefono_cliente = datos.get('telefono_cliente')
        representante_cliente = datos.get('representante_cliente')
        direccion = datos.get('direccion')
        cli=cliente.objects.create(id_cliente=id_cliente, nombre_cliente=nombre_cliente, telefono_cliente=telefono_cliente, representante_cliente=representante_cliente, direccion=direccion)
        cli.save()
        return JsonResponse({'mensaje': 'datos guardados'})

def formularioInsertarCli(request):
    return render(request,"insertarCli.html")    








class listarProveedor(ListView):
    def get(self,request):
        datos=proveedor.objects.all()
        datos_proveedor=[]
        for i in datos:
            datos_proveedor.append({ 
                'nombre_proveedor':i.nombre_proveedor,
                'telefono_proveedor':i.telefono_proveedor,
            }) 
        return JsonResponse(datos_proveedor, safe=False)
        

class InsertarProveedor(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    def post(self, request):
        try:
            datos=json.loads(request.body)
        except(json.JSONDecodeError,UnicodeDecodeError):
            return JsonResponse({"error": "Error en la decodificacion"})
        nombre_proveedor = datos.get('nombre_proveedor')
        telefono_proveedor = datos.get('telefono_proveedor')
        prov=proveedor.objects.create(nombre_proveedor=nombre_proveedor, telefono_proveedor=telefono_proveedor)
        prov.save()
        return JsonResponse({'mensaje': 'datos guardados'})

def formularioInsertarProv(request):
    return render(request,"insertarProve.html")    









class listarMaterial(ListView):
    def get(self,request):
        datos=material.objects.all()
        datos_material=[]
        for i in datos:
            datos_material.append({ 
                'codi_mate':i.codi_mate,
                'nomb_mate':i.nomb_mate,
                'cant_mate':i.cant_mate,
                'proveedor_mate':i.proveedor_mate,
            }) 
        return JsonResponse(datos_material, safe=False)
        

class InsertarMaterial(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    def post(self, request):
        try:
            datos=json.loads(request.body)
        except(json.JSONDecodeError,UnicodeDecodeError):
            return JsonResponse({"error": "Error en la decodificacion"})
        codi_mate = datos.get('codi_mate')
        nomb_mate = datos.get('nomb_mate')
        cant_mate = datos.get('cant_mate')
        proveedor_mate = datos.get('proveedor_mate')
        mate=material.objects.create(codi_mate=codi_mate, nomb_mate=nomb_mate, cant_mate=cant_mate, proveedor_mate=proveedor_mate)
        mate.save()
        return JsonResponse({'mensaje': 'datos guardados'})

def formularioInsertarMate(request):
    return render(request,"insertarMate.html")    











class listarProducto(ListView):
    def get(self,request):
        datos=producto.objects.all()
        datos_producto=[]
        for i in datos:
            datos_producto.append({ 
                'codi_prod':i.codi_prod,
                'nomb_prod':i.nomb_prod,
                'tiempo_prod':i.tiempo_prod,
                'long_prod':i.long_prod,
                'material_prod':i.long_prod,
                'prec_prod':i.long_prod,
            }) 
        return JsonResponse(datos_producto, safe=False)
        

class InsertarProducto(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    def post(self, request):
        try:
            datos=json.loads(request.body)
        except(json.JSONDecodeError,UnicodeDecodeError):
            return JsonResponse({"error": "Error en la decodificacion"})
        codi_prod = datos.get('codi_prod')
        nomb_prod = datos.get('nomb_prod')
        tiempo_prod = datos.get('tiempo_prod')
        long_prod = datos.get('long_prod')
        material_prod = datos.get('material_prod')
        prec_prod = datos.get('prec_prod')
        mate=material.objects.create(codi_prod=codi_prod, nomb_prod=nomb_prod, tiempo_prod=tiempo_prod, long_prod=long_prod,material_prod=material_prod, prec_prod=prec_prod)
        mate.save()
        return JsonResponse({'mensaje': 'datos guardados'})

def formularioInsertarProd(request):
    return render(request,"insertarProd.html")    







class listarPedido(ListView):
    def get(self,request):
        datos=pedido.objects.all()
        datos_pedido=[]
        for i in datos:
            datos_pedido.append({ 
                'id_pedido':i.id_pedido,
                'cliente_pedido':i.cliente_pedido,
                'producto_pedido':i.producto_pedido,
                'usuario_pedido':i.usuario_pedido,
                'tiempo_pedido':i.tiempo_pedido,
                'fecha_encargo':i.fecha_encargo,
                'fecha_entrega':i.fecha_entrega,
            }) 
        return JsonResponse(datos_pedido, safe=False)
        

class InsertarPedido(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    def post(self, request):
        try:
            datos=json.loads(request.body)
        except(json.JSONDecodeError,UnicodeDecodeError):
            return JsonResponse({"error": "Error en la decodificacion"})
        id_pedido = datos.get('id_pedido')
        cliente_pedido = datos.get('cliente_pedido')
        producto_pedido = datos.get('producto_pedido')
        usuario_pedido = datos.get('usuario_pedido')
        tiempo_pedido = datos.get('tiempo_pedido')
        fecha_encargo = datos.get('fecha_encargo')
        fecha_entrega = datos.get('fecha_entrega')
        pedi=pedido.objects.create(id_pedido=id_pedido, cliente_pedido=cliente_pedido, producto_pedido=producto_pedido, usuario_pedido=usuario_pedido, tiempo_pedido=tiempo_pedido,fecha_encargo=fecha_encargo,fecha_entrega=fecha_entrega)
        pedi.save()
        return JsonResponse({'mensaje': 'datos guardados'})

def formularioInsertarPedi(request):
    return render(request,"insertarPedi.html") 









# class Actualizar(View):
#     @method_decorator(csrf_exempt)
#     def dispatch(self, request, *args: Any, **kwargs):
#         return super().dispatch(request, *args, **kwargs)
    
#     def put(self,request,pk):
#         try:
#             registro=usuario.objects.get(pk=pk)

#         except usuario.DoesNotExist:
#             return JsonResponse({"Error": "El documento no existe"})
        
#         data=json.loads(request.body)
#         registro.nombre=data.get('nombre_usuario')
#         registro.correo=data.get('correo_usuario')
#         registro.password=data.get('pass_ususario')
#         registro.tipo=data.get('tipo_usuario')
#         registro.save()
#         return JsonResponse({"mensaje": "datos  del usuario actualizados"})


