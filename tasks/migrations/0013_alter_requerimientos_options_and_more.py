# Generated by Django 5.0.2 on 2024-03-15 20:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0012_pruebas'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='requerimientos',
            options={'verbose_name': 'Requerimiento', 'verbose_name_plural': 'Requerimientos'},
        ),
        migrations.AlterModelTable(
            name='requerimientos',
            table='Requerimientos',
        ),
    ]