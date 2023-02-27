from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.postgres.fields import ArrayField


class Hospedado(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    nome_hospede = models.CharField(max_length=200)
    habilitado = models.BooleanField(default=True)
    status = models.CharField(max_length=200, default='reservado')
    numero_quarto = models.CharField(max_length=200)
    valor_quarto = models.FloatField()
    valor_comanda = models.FloatField()
    diarias = models.IntegerField()
    data_reserva= models.DateTimeField(default=timezone.now)
    data_entrada = models.DateField()
    data_saida = models.DateField()

    def dt_reserva(self):
        self.data_reserva = timezone.now()
        self.save()




class Quarto(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    data_criacao = models.DateTimeField(default=timezone.now)
    habilitado = models.BooleanField(default=True)
    numero = models.IntegerField()
    tipo = models.CharField(max_length=200)
    capacidade = models.IntegerField(default=0)
    descricao = models.CharField(max_length=200, default="")

    def criacao(self):
        self.data_criacao = timezone.now()
        self.save()



class Endereco (models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    data_criacao = models.DateTimeField(default=timezone.now)
    habilitado = models.BooleanField(default=True)
    cep = models.CharField(max_length=200)
    rua = models.CharField(max_length=200)
    complemento = models.CharField(max_length=200)
    cidade = models.CharField(max_length=200)
    estado = models.CharField(max_length=200)
    pais = models.CharField(max_length=200, default="Brasil")



class Hospede (models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    data_criacao = models.DateTimeField(default=timezone.now)
    habilitado = models.BooleanField(default=True)
    nome = models.CharField(max_length=200)
    sexo = models.CharField(max_length=200, default="Não Informado")
    data_aniversario = models.DateField()
    cpf = models.CharField(max_length=200, default="null")
    rg = models.CharField(max_length=200, default="null")
    telefone = models.CharField(max_length=200, default="null")
    email = models.CharField(max_length=200, default="null")
    endereco = models.ForeignKey(Endereco, on_delete=models.PROTECT)




class Reserva (models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    data_criacao = models.DateField(default=timezone.now)
    quarto = models.ForeignKey(Quarto, on_delete=models.PROTECT)
    habilitado = models.BooleanField(default=True)
    quantidade_hospedes = models.IntegerField(default=1)
    data_entrada = models.DateField(blank=True, null=False)
    data_saida = models.DateField(blank=True, null=False)
    diarias = models.IntegerField()
    valor = models.FloatField(default=0)

class Reserva_pendente (models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    data_criacao = models.DateField(default=timezone.now)
    habilitado = models.BooleanField(default=True)
    data_entrada = models.DateField(blank=True, null=False)
    quantidade_hospedes = models.IntegerField(default=0)
    data_saida = models.DateField(blank=True, null=False)
    diarias = models.IntegerField(default = 0, blank=True, null=False)


class Hospedes_reserva(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    habilitado = models.BooleanField(default=True)
    data_criacao = models.DateTimeField(default=timezone.now)
    reserva = models.ForeignKey(Reserva, on_delete=models.PROTECT)
    hospede = models.ForeignKey(Hospede, on_delete=models.PROTECT)
    status = models.CharField(max_length=200, default="EM ABERTO")
    valor_comanda = models.FloatField(default=0)
    valor_total = models.FloatField(default=0)
    


class Produto (models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    data_criacao = models.DateTimeField(default=timezone.now)
    habilitado = models.BooleanField(default=True)
    nome = models.CharField(max_length=200)
    valor_venda = models.FloatField(default=0)
    valor_custo = models.FloatField(default=0)
    descricao = models.CharField(max_length=200)




class Comanda_consumo(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    data_criacao = models.DateTimeField(default=timezone.now)
    habilitado = models.BooleanField(default=True)
    hospedes_reserva = models.ForeignKey(Hospedes_reserva, on_delete=models.PROTECT)
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT)

class Fechamento_conta (models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    data_criacao = models.DateTimeField(default=timezone.now)
    habilitado = models.BooleanField(default=True)
    hospedes_reserva = models.ForeignKey(Hospedes_reserva, on_delete=models.PROTECT)
    pago = models.BooleanField(default=False)
    valor_consumo = models.FloatField()
    valor_diarias = models.FloatField()
    desconto_conta = models.FloatField()
    descricao_extra = models.TextField(max_length=2000)
