# Generated by Django 3.2.17 on 2023-02-23 00:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('core', '0023_auto_20230222_2117'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospedes_reserva',
            name='valor_total',
            field=models.IntegerField(default=0),
        ),
    ]
