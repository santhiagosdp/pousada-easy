# Generated by Django 3.2.17 on 2023-02-23 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0024_hospedes_reserva_valor_total'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produto',
            name='valor',
        ),
        migrations.AddField(
            model_name='produto',
            name='valor_custo',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='produto',
            name='valor_venda',
            field=models.FloatField(default=0),
        ),
    ]