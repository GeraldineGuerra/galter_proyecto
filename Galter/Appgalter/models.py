from django.db import models


class usuario(models.Model):
    codi_usuario = models.TextField(max_length=10, primary_key=True)
    nombre_usuario = models.TextField(max_length=50)
    correo_usuario = models.EmailField(max_length=50)
    pass_usuario = models.TextField(max_length=100)
    tipo_usuario = models.TextField(max_length=30)






class cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nombre_cliente = models.TextField(max_length=50)
    telefono_cliente = models.TextField(max_length=15)
    representante_cliente = models.TextField(max_length=50)
    direccion = models.TextField(max_length=50)



class proveedor(models.Model):
    nombre_proveedor = models.TextField(max_length=50, primary_key=True)
    telefono_proveedor = models.TextField(max_length=15)





class material(models.Model):
    codi_mate = models.TextField(max_length=10, primary_key=True)
    nomb_mate = models.TextField(max_length=50)
    cant_mate = models.TextField(max_length=10)
    proveedor_mate = models.TextField(max_length=50)
    #proveedor_mate = models.ForeignKey(proveedor, null=False,on_delete=models.CASCADE)





class producto(models.Model):
    codi_prod = models.TextField(max_length=10, primary_key=True)
    nomb_prod = models.TextField(max_length=100)
    tiempo_prod = models.TextField(max_length=50)
    long_prod = models.TextField(max_length=10)
    material_prod = models.TextField(max_length=50)
    #material_prod = models.ForeignKey(material, null=False,on_delete=models.CASCADE)
    prec_prod = models.TextField(max_length=10)




class pedido(models.Model):
    id_pedido = models.AutoField(primary_key=True)
    cliente_pedido = models.ForeignKey(cliente, null=False,on_delete=models.CASCADE)
    producto_pedido = models.ForeignKey(producto, null=False,on_delete=models.CASCADE)
    usuario_pedido = models.ForeignKey(usuario, null=False,on_delete=models.CASCADE)
    tiempo_pedido = models.TextField(max_length=10)
    fecha_encargo = models.TextField(max_length=10)
    fecha_entrega = models.TextField(max_length=10)