from django.contrib import admin

from .models import Hospedado, Quarto, Hospede,Endereco,Reserva,Hospedes_reserva, Produto, Comanda_consumo, Fechamento_conta

admin.site.register(Hospedado),

class QuartoAdmin(admin.ModelAdmin):
    list_display = ("data_criacao", "numero", "tipo","capacidade","descricao","habilitado", )
admin.site.register(Quarto, QuartoAdmin),


class HospedeAdmin(admin.ModelAdmin):
    list_display = ("data_criacao", "nome", "cpf","rg","telefone","email","habilitado", )
admin.site.register(Hospede, HospedeAdmin),

admin.site.register(Endereco),
admin.site.register(Reserva),
admin.site.register(Hospedes_reserva),
admin.site.register(Produto),
admin.site.register(Comanda_consumo),
admin.site.register(Fechamento_conta)

