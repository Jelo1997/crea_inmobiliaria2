# Generated by Django 3.2.24 on 2024-02-08 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crea_admin', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propiedad',
            name='precio',
            field=models.DecimalField(decimal_places=2, max_digits=65),
        ),
    ]
