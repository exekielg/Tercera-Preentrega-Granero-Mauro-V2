# Generated by Django 4.1.7 on 2023-03-14 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TiendaApp', '0005_alter_producto_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='TiendaApp/static/TiendaApp/img/products'),
        ),
    ]
