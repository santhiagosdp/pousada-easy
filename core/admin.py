from django.contrib import admin

from .models import Hospedado, Quarto, Hospede,Endereco,Reserva,Hospedes_reserva, Produto, Comanda_consumo, Fechamento_conta

admin.site.register(Hospedado),
admin.site.register(Quarto),
admin.site.register(Hospede),
admin.site.register(Endereco),
admin.site.register(Reserva),
admin.site.register(Hospedes_reserva),
admin.site.register(Produto),
admin.site.register(Comanda_consumo),
admin.site.register(Fechamento_conta)

