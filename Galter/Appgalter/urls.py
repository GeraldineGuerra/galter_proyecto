from django.urls import path
from Appgalter.views import listarUsuarios, InsertarUsuario, InsertarCliente,listarClientes,listarProveedor,InsertarProveedor,listarMaterial,InsertarMaterial,InsertarProducto,listarProducto,listarpedido,InsertarPedido
from Appgalter.views import listarUsuario2
from . import views



urlpatterns = [
    #mostrar con html
    path('Usuario1', listarUsuario2.as_view(), name='Usuario1'),



    #listar
    path('Usuario', listarUsuarios.as_view(), name='Usuario'),
    path('Cliente', listarClientes.as_view(), name='Clientes'),
    path('Proveedor', listarProveedor.as_view(), name='Proveedor'),
    path('Material', listarMaterial.as_view(), name='Material'),
    path('Producto', listarProducto.as_view(), name='Prooducto'),
    path('Pedido', listarpedido.as_view(), name='Pedido'),




    #insertar
    path('insertarUsu/', InsertarUsuario.as_view(), name='insertarUsu'),
    path('insertarCli/', InsertarCliente.as_view(), name='insertarCli'),
    path('insertarProv/', InsertarProveedor.as_view(), name='insertarProv'),
    path('insertarMate/', InsertarMaterial.as_view(), name='insertarMate'),
    path('insertarProd/', InsertarProducto.as_view(), name='insertarProd'),
    path('insertarPedi/', InsertarPedido.as_view(), name='insertarPedi'),




    #insertar datos con js
    path('frmInsertar',views.formularioInsertar, name='resgistrar'),
    path('frmClientes',views.formularioInsertarCli, name='resgistrarCli'),
    path('frmProveedor',views.formularioInsertarProv, name='resgistrarProv'),
    path('frmMaterial',views.formularioInsertarMate, name='resgistrarMate'),
    path('frmProducto',views.formularioInsertarProd, name='resgistrarProd'),
    path('frmPedido',views.formularioInsertarPedi, name='resgistrarPedi'),
    
    
    
]
