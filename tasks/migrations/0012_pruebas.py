# Generated by Django 5.0.2 on 2024-03-11 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0011_alter_alianzasolicitante_alianzasolicitante_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pruebas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=50)),
            ],
            options={
                'verbose_name': 'Prueba',
                'verbose_name_plural': 'Prueba T',
            },
        ),
    ]
