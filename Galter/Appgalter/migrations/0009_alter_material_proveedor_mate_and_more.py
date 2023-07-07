# Generated by Django 4.1.7 on 2023-06-27 15:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Appgalter', '0008_alter_producto_material_prod'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='proveedor_mate',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Appgalter.proveedor'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='material_prod',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Appgalter.material'),
        ),
    ]
