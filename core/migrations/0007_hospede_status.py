# Generated by Django 3.2.17 on 2023-02-10 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_hospede_sexo'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospede',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
