# Generated by Django 3.2.17 on 2023-02-17 12:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('core', '0019_reserva_pendente_quantidade_hospedes'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserva_pendente',
            name='diarias',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
