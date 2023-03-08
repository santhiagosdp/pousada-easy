# from django.contrib import admin
from django.urls import path, include

from core import views
from django.contrib.auth import views as auth_views

# from django.conf import settings


urlpatterns = [

    path('accounts/', include('django.contrib.auth.urls')),  # LOGIN
    path('accounts/logout', views.logout_view, name='logout'),  # LOGOUT
    path('accounts/editar/perfil', views.edit_user, name='edit_user'),  # edit_user
    path('accounts/editar/empresa', views.edit_empresa, name='edit_empresa'),  # edit_empresa


    #REETAR SENHA
    path('password_reset', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),


    path('', views.home, name='home'),  # HOME

    path('cadastrar_usuario', views.cadastrar_usuario, name='cadastrar_usuario'),

    path('clientes', views.clientes, name='clientes'),
    path('cliente/delete/<id>', views.cliente_delete, name='cliente_delete'),

    path('quartos', views.quartos, name='quartos'),
    path('quarto/edit/<id>', views.quarto_edit, name='quarto_edit'),
    path('quarto/delete/<id>', views.quarto_delete, name='quarto_delete'),

    path('produtos', views.produtos, name='produtos'),
    path('produto/delete/<id>', views.produto_delete, name='produto_delete'),
    path('produto/edit/<id>', views.produto_edit, name='produto_edit'),


    path('reservar', views.reservar, name='reservar'),
    # path('reservando_dados/<id>', views.reservando_dados, name='reservando_dados'),
    path('disponibilidade/', views.disponibilidade, name='disponibilidade'),
    path('hospedagem/delete/<id>', views.hospedagem_delete, name='hospedagem_delete'),

    path('hospedagem/checkin/<id>', views.hospedagem_checkin, name='hospedagem_checkin'),
    path('hospedagem/checkout/<id>', views.fechar_conta_checkout, name='fechar_conta_checkout'), #checkout
    path('hospedagem/concluir/<id>', views.hospedagem_concluir, name='hospedagem_concluir'), #checkout


    path('comandas', views.comandas, name='comandas'),
    path('comanda/hospedagem/<id>', views.itenscomanda, name='itenscomanda'),
    path('comanda/produto/delete/<idcomandaconsumo>/<idhospede>', views.comanda_produto_delete,name='comanda_produto_delete'),

    

    

    path('<path:unknown_path>', views.home),

]

'''if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()'''
