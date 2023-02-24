#from django.contrib import admin
from django.urls import path, include
from .views import *
from core import views
#from django.conf import settings


urlpatterns = [

    path('accounts/', include('django.contrib.auth.urls')), #LOGIN
    path('accounts/logout', views.logout_view, name='logout'), #LOGOUT
    path('', views.home, name='home'), #HOME

    path('cadastrar_usuario/', views.cadastrar_usuario, name='cadastrar_usuario'),

    path('clientes/', views.clientes, name='clientes'),
    path('cliente/delete/<id>', views.cliente_delete, name='cliente_delete'),

    path('quartos/', views.quartos, name='quartos'),
    path('quarto/delete/<id>', views.quarto_delete, name='quarto_delete'),

    path('produtos/', views.produtos, name='produtos'),
    path('produto/delete/<id>', views.produto_delete, name='produto_delete'),

    path('reservar', views.reservar, name='reservar'),
    #path('reservando_dados/<id>', views.reservando_dados, name='reservando_dados'),
    path('disponibilidade', views.disponibilidade, name='disponibilidade'),
    path('hospedagem/delete/<id>', views.hospedagem_delete, name='hospedagem_delete'),

    path('comandas/', views.comandas, name='comandas'),


    

    

    
    


    path('<path:unknown_path>', views.home),

    



]


'''if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()'''