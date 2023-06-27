from django.contrib import admin
from Appgalter.models import usuario
from Appgalter.models import cliente, material, pedido, producto, proveedor



@admin.register(usuario)
class usuraioadmin(admin.ModelAdmin):
    list_display=('codi_usuario', 'nombre_usuario', 'correo_usuario','pass_usuario', 'tipo_usuario')
    #ordering=('-nombre',)
    #ordering=('nombre', 'apellido')
    #search_fields=('nombre_usuario',)
    #list_display_links=('documento',)
    #list_editable=('nombre', 'apellido', 'correo','celular')
    #list_filter=('nombre',)
    #list_per_page=3




@admin.register(proveedor)
class proveedoradmin(admin.ModelAdmin):
    #list_display = ('nombre_proveedor') 
    #ordering=('-nombre',)
    #ordering=('nombre', 'apellido')
    search_fields=('nombre_proveedor',)
    #list_display_links=('documento',)
    #list_editable=('nombre', 'apellido', 'correo','celular')
    #list_filter=('nombre',)
    #list_per_page=3




@admin.register(cliente)
class clienteadmin(admin.ModelAdmin):
    list_display=('id_cliente','nombre_cliente','telefono_cliente','representante_cliente','direccion')





@admin.register(material)
class materialadmin(admin.ModelAdmin):
    list_display = ('codi_mate','nomb_mate')



@admin.register(producto)
class productoadmin(admin.ModelAdmin):
    list_display=('codi_prod','nomb_prod','tiempo_prod','long_prod','material_prod','prec_prod')





@admin.register(pedido)
class pedidoadmin(admin.ModelAdmin):
    list_display=('id_pedido','cliente_pedido','producto_pedido','tiempo_pedido','fecha_encargo','fecha_entrega')
