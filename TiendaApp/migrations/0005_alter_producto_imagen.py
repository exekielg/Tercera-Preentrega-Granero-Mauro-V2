# Generated by Django 4.1.7 on 2023-03-13 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TiendaApp', '0004_rename_nombre_producto_marca_producto_modelo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='TiendaApp/media'),
        ),
    ]