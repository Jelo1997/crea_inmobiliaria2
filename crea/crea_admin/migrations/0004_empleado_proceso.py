# Generated by Django 5.0.2 on 2024-02-09 04:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crea_admin', '0003_alter_caracteristicas_nombre_alter_servicios_nombre'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('User', 'User'), ('Admin', 'Admin')], max_length=15)),
                ('username', models.CharField(max_length=144)),
                ('email', models.EmailField(max_length=144)),
                ('password', models.CharField(max_length=144)),
                ('telefono', models.CharField(max_length=144)),
            ],
        ),
        migrations.CreateModel(
            name='Proceso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=144)),
                ('descripcion', models.CharField(max_length=144)),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('estado', models.CharField(choices=[('En Curso', 'En Curso'), ('Finalizado', 'Finalizado')], max_length=25)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pk', to='crea_admin.cliente')),
                ('propiedad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pk', to='crea_admin.propiedad')),
            ],
        ),
    ]
