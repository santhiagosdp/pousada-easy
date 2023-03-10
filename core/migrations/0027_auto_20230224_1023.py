# Generated by Django 3.2.17 on 2023-02-24 13:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('core', '0026_auto_20230223_1657'),
    ]

    operations = [
        migrations.AddField(
            model_name='comanda_consumo',
            name='habilitado',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='endereco',
            name='habilitado',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='fechamento_conta',
            name='habilitado',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='hospedado',
            name='habilitado',
            field=models.BooleanField(default=True),
        ),
    ]
