# Generated by Django 5.0.7 on 2024-10-22 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vams', '0003_clientes_empleados_factura'),
    ]

    operations = [
        migrations.AddField(
            model_name='productos',
            name='imagen_producto',
            field=models.ImageField(default='default.jpg', upload_to='productos/'),
        ),
        migrations.AlterField(
            model_name='productos',
            name='categoria_producto',
            field=models.CharField(choices=[('Collares', 'Collares'), ('Aretes', 'Aretes')], default='Collares', max_length=200),
        ),
    ]
