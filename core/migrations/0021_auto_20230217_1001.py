# Generated by Django 3.2.17 on 2023-02-17 13:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('core', '0020_reserva_pendente_diarias'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='diarias',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='valor',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
