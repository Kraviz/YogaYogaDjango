# Generated by Django 4.2.2 on 2023-06-28 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0003_alter_producto_options_producto_descripcion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='img',
            field=models.ImageField(blank=True, default='', null=True, upload_to='productos', verbose_name='imagen'),
        ),
    ]