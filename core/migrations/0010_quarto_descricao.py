# Generated by Django 3.2.17 on 2023-02-10 18:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('core', '0009_rename_habilitato_hospede_habilitado'),
    ]

    operations = [
        migrations.AddField(
            model_name='quarto',
            name='descricao',
            field=models.CharField(default='', max_length=200),
        ),
    ]
