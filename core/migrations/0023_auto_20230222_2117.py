# Generated by Django 3.2.17 on 2023-02-23 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_auto_20230217_1006'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospedes_reserva',
            name='status',
            field=models.CharField(default='Em Aberto', max_length=200),
        ),
        migrations.AddField(
            model_name='hospedes_reserva',
            name='valor_comanda',
            field=models.IntegerField(default=0),
        ),
    ]
