#from django.contrib import admin
from django.urls import path, include
from .views import *
from core import views
#from django.conf import settings


urlpatterns = [
    path('cadastrar_usuario/', views.cadastrar_usuario, name='cadastrar_usuario'),
    path('clientes/', views.clientes, name='clientes'),
    path('cliente/delete/<id>', views.cliente_delete, name='clientes'),

    path('accounts/', include('django.contrib.auth.urls')), #LOGIN
    path('accounts/logout', views.logout_view, name='logout'), #LOGOUT
    path('', views.home, name='home'), #HOME

    path('reservar', views.reservar, name='reservar'),
    path('disponibilidade', views.disponibilidade, name='disponibilidade'),


    



]


'''if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()'''