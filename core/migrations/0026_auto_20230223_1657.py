# Generated by Django 3.2.17 on 2023-02-23 19:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('core', '0025_auto_20230223_1328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospedes_reserva',
            name='valor_comanda',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='hospedes_reserva',
            name='valor_total',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='valor',
            field=models.FloatField(default=0),
        ),
    ]
