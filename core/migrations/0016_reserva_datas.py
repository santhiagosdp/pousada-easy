# Generated by Django 3.2.17 on 2023-02-14 19:06

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('core', '0015_auto_20230213_1134'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserva',
            name='datas',
            field=django.contrib.postgres.fields.ArrayField(
                base_field=django.contrib.postgres.fields.ArrayField(base_field=models.DateField(), size=365),
                default='2023-02-02', size=365),
            preserve_default=False,
        ),
    ]
