# Generated by Django 5.0.2 on 2024-03-06 03:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0009_rename_alianzasolicitante_alianzasolicitante_alianzasolicitante_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='requerimientos',
            old_name='fechaactualizacion',
            new_name='fecha_actualizacion',
        ),
        migrations.RenameField(
            model_name='requerimientos',
            old_name='pasosroduccion',
            new_name='pasoproduccion',
        ),
    ]