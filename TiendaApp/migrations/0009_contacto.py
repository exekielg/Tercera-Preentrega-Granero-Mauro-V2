# Generated by Django 4.1.7 on 2023-04-09 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TiendaApp', '0008_remove_cliente_fnacimiento_alter_producto_imagen'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('telefono', models.CharField(max_length=20)),
            ],
        ),
    ]
