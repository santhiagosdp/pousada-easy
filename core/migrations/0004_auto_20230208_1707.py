# Generated by Django 3.2.17 on 2023-02-08 20:07

import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0003_rename_estatus_hospedado_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_criacao', models.DateTimeField(default=django.utils.timezone.now)),
                ('cep', models.CharField(max_length=200)),
                ('rua', models.CharField(max_length=200)),
                ('complemento', models.CharField(max_length=200)),
                ('cidade', models.CharField(max_length=200)),
                ('estado', models.CharField(max_length=200)),
                ('pais', models.CharField(default='Brasil', max_length=200)),
                (
                'usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Hospede',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_criacao', models.DateTimeField(default=django.utils.timezone.now)),
                ('nome', models.CharField(max_length=200)),
                ('data_aniversario', models.DateField()),
                ('cpf', models.CharField(default='null', max_length=200)),
                ('rg', models.CharField(default='null', max_length=200)),
                ('email', models.CharField(default='null', max_length=200)),
                ('endereco', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.endereco')),
                (
                'usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Quarto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_criacao', models.DateTimeField(default=django.utils.timezone.now)),
                ('numero', models.IntegerField()),
                ('tipo', models.CharField(max_length=200)),
                ('pessoas_suporta', models.IntegerField()),
                (
                'usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='hospedado',
            name='data_entrada',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='hospedado',
            name='data_saida',
            field=models.DateField(),
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_criacao', models.DateTimeField(default=django.utils.timezone.now)),
                ('data_entrada', models.DateTimeField(blank=True)),
                ('data_saida', models.DateTimeField(blank=True)),
                ('diarias', models.IntegerField()),
                ('valor', models.FloatField()),
                ('quarto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.quarto')),
                (
                'usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_criacao', models.DateTimeField(default=django.utils.timezone.now)),
                ('nome', models.CharField(max_length=200)),
                ('valor', models.FloatField()),
                ('descricao', models.CharField(max_length=200)),
                (
                'usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Hospedes_reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_criacao', models.DateTimeField(default=django.utils.timezone.now)),
                ('hospede', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.hospede')),
                ('reserva', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.reserva')),
                (
                'usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Fechamento_conta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_criacao', models.DateTimeField(default=django.utils.timezone.now)),
                ('valor_consumo', models.FloatField()),
                ('valor_diarias', models.FloatField()),
                ('desconto_conta', models.FloatField()),
                ('descricao_extra', models.TextField(max_length=2000)),
                ('hospedes_reserva',
                 models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.hospedes_reserva')),
                (
                'usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comanda_consumo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_criacao', models.DateTimeField(default=django.utils.timezone.now)),
                ('hospedes_reserva',
                 models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.hospedes_reserva')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.produto')),
                (
                'usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
