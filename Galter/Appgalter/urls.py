from django.urls import path
from Appgalter.views import *
from Appgalter.viewsAuth import *
from . import views
from django.conf import *
from django.conf.urls.static import *



urlpatterns = [
    
    #listar
    path('Usuario', listarUsuarios.as_view(), name='Usuario'),
    path('Cliente', listarClientes.as_view(), name='Clientes'),
    path('Proveedor', listarProveedor.as_view(), name='Proveedor'),
    path('Material', listarMaterial.as_view(), name='Material'),
    path('Producto', listarProducto.as_view(), name='Productos'),
    path('Pedido', listarpedido.as_view(), name='Pedido'),


    path('produc', listarProductoo.as_view(), name='prod'),




    #insertar
    path('insertarUsu/', InsertarUsuario.as_view(), name='insertarUsu'),
    path('insertarCli/', InsertarCliente.as_view(), name='insertarCli'),
    path('insertarProv/', InsertarProveedor.as_view(), name='insertarProv'),
    path('insertarMate/', InsertarMaterial.as_view(), name='insertarMate'),

    path('insertarProd/', InsertarProducto.as_view(), name='insertarProducto'),
    path('insertarPedi/', InsertarPedido.as_view(), name='insertarPedi'),




    #insertar datos con js
    path('frmInsertar',views.formularioInsertar, name='resgistrar'),
    path('frmClientes',views.formularioInsertarCli, name='resgistrarCli'),
    path('frmProveedor',views.formularioInsertarProv, name='resgistrarProv'),
    path('frmMaterial',views.formularioInsertarMate, name='resgistrarMate'),
    
    path('frmPedido',views.formularioInsertarPedi, name='resgistrarPedi'),




    path('index', views.index, name='principal'),
    path('frmProducto',views.formularioInsertarProd, name='resgistrarProd'),
    path('registro', views.registro, name='registrar'),
    path('codigo', views.codigo, name='codiVeri'),
    path('menu', views.menu, name='menus'),
    path('masOpciones', views.masOpciones, name='masOp'),
    path('opcionesProd', views.opcionesProd, name='opciProd'),

    

    path('registroUser/',RegistrarUsuarioView.as_view(), name="registrar_usuario"),
    path('iniciarSesion/', IniciarSesionView.as_view(),name='iniciar_sesion'),
    path('updateUsuario/', PerfilUsuarioView.as_view(), name="update_usuario")


]+ static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
