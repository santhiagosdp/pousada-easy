# Generated by Django 3.2.17 on 2023-02-24 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0027_auto_20230224_1023'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserva',
            name='quantidade_hospedes',
            field=models.IntegerField(default=1),
        ),
    ]