# Generated by Django 5.0.2 on 2024-03-05 02:32

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0007_requerimientos_alianzasolicitante_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='requerimientos',
            name='alianzaSolicitante',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='tasks.alianzasolicitante', verbose_name='Alianza'),
        ),
        migrations.AlterField(
            model_name='requerimientos',
            name='areaSolicitante',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='tasks.areasolicitante', verbose_name='Area'),
        ),
        migrations.AlterField(
            model_name='requerimientos',
            name='estado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='tasks.estado', verbose_name='Estado De Ejecución'),
        ),
        migrations.AlterField(
            model_name='requerimientos',
            name='fechaActualizacion',
            field=models.DateTimeField(auto_now=True, verbose_name='Fecha Actualización BD'),
        ),
        migrations.AlterField(
            model_name='requerimientos',
            name='fechaCreacion',
            field=models.DateField(verbose_name='Fecha Creación'),
        ),
        migrations.AlterField(
            model_name='requerimientos',
            name='fechaPruebas',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha Pruebas'),
        ),
        migrations.AlterField(
            model_name='requerimientos',
            name='fechaRegistro',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Fecha Registro BD'),
        ),
        migrations.AlterField(
            model_name='requerimientos',
            name='medioCarga',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='tasks.mediocarga', verbose_name='Medio De Carga'),
        ),
        migrations.AlterField(
            model_name='requerimientos',
            name='observaciones',
            field=models.TextField(blank=True, null=True, verbose_name='Observaciones y/o Avances'),
        ),
        migrations.AlterField(
            model_name='requerimientos',
            name='pasoProduccion',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha Paso Producción'),
        ),
        migrations.AlterField(
            model_name='requerimientos',
            name='plataforma',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='tasks.plataforma', verbose_name='Plataforma'),
        ),
        migrations.AlterField(
            model_name='requerimientos',
            name='requerimiento',
            field=models.CharField(blank=True, max_length=100, verbose_name='Nombre Requerimiento'),
        ),
        migrations.AlterField(
            model_name='requerimientos',
            name='responsable',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='tasks.responsable', verbose_name='Responsable'),
        ),
        migrations.AlterField(
            model_name='requerimientos',
            name='sprintDesarrollo',
            field=models.CharField(choices=[('Sin Sprint', 'Sin Sprint'), ('Enero', 'Enero'), ('Febrero', 'Febrero')], default='Sin Sprint', max_length=100, verbose_name='Sprint Desarrollo'),
        ),
        migrations.AlterField(
            model_name='requerimientos',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario'),
        ),
    ]
