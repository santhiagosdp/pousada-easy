# Generated by Django 3.2.17 on 2023-02-10 03:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('core', '0005_hospede_telefone'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospede',
            name='sexo',
            field=models.CharField(default='Não Informado', max_length=200),
        ),
    ]
