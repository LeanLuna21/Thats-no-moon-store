# Generated by Django 4.2.7 on 2024-01-10 21:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0002_producto_imagen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='imagen',
        ),
    ]
