# Generated by Django 4.1.7 on 2023-06-06 14:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Appgalter', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='material',
            old_name='proveedor',
            new_name='proveedor_mate',
        ),
        migrations.RenameField(
            model_name='pedido',
            old_name='producto',
            new_name='producto_pedido',
        ),
    ]
