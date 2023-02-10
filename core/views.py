from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from datetime import datetime

from .models import Hospedado, Quarto, Hospede,Endereco,Reserva,Hospedes_reserva, Produto, Comanda_consumo, Fechamento_conta

# Create your views here.


def cadastrar_usuario(request):
    if request.method == "POST":
        form_usuario = UserCreationForm(request.POST)
        if form_usuario.is_valid():
            form_usuario.save()
            return redirect('home')
    else:
        form_usuario = UserCreationForm()
    return render(request, 'core/cadastro.html', {'form_usuario': form_usuario})

@login_required
def home(request):
    #HOMEEEEE

    return render(request, 'core/home.html', {'titulo':'Home'})


@login_required
def clientes(request):
    ##CADASTRO DE CLIENTE POST
    if request.method == 'POST':
        nome = request.POST.get("nome")
        cpf = request.POST.get("cpf")
        rg = request.POST.get("rg")
        data_aniversario = request.POST.get("data_aniversario")
        sexo = request.POST.get("sexo")
        email = request.POST.get("email")
        telefone = request.POST.get("telefone")

        cep = request.POST.get("cep")
        cidade = request.POST.get("cidade")
        estado = request.POST.get("estado")
        rua = request.POST.get("endereco")
        complemento = request.POST.get("complemento")
        
        endereco_cad =Endereco.objects.create(
                usuario = request.user,
                cep = cep,
                cidade = cidade,
                estado = estado,
                rua = rua,
                complemento = complemento)
        endereco_cad.save

        hospede_cad = Hospede.objects.create(
                usuario = request.user,
                habilitado = True,
                nome = nome,
                cpf = cpf,
                rg = rg,
                data_aniversario = data_aniversario,
                sexo = sexo,
                email = email,
                telefone = telefone,
                endereco = endereco_cad)
        hospede_cad.save
        return redirect('clientes') 
    #####FIM DO CADASTRO DO CLIENTE


    hospedes = Hospede.objects.filter(habilitado = True, usuario=request.user).order_by('nome')

    ## botão de buscar hospede get
    buscar = request.GET.get('search')
    if buscar:
        hospedes = Hospede.objects.filter(habilitado = True, usuario=request.user, nome__icontains = buscar).order_by('nome')
    ####### FIM DO BUSCAR

    return render(request, 'core/clientes.html', {'titulo':'Clientes', 'hospedes':hospedes})


@login_required
def quartos(request):    
    ##CADASTRO DE QUARTO POST
    if request.method == 'POST':   
        quarto_cad = Quarto.objects.create(
                usuario = request.user,
                tipo = request.POST.get("tipo"),
                numero = request.POST.get("numero"),
                capacidade = request.POST.get("capacidade"),
                descricao = request.POST.get("descricao")
        )
        quarto_cad.save

        return redirect('quartos') 
    #####  FIM DO CADASTRO DO QUARTO


    quartos = Quarto.objects.filter(habilitado = True, usuario=request.user).order_by('numero')

    ## botão de buscar hospede get
    buscar = request.GET.get('search')
    if buscar:
        quartos = Quarto.objects.filter(habilitado = True, usuario=request.user, numero__icontains = buscar).order_by('numero')
    ####### FIM DO BUSCAR

    return render(request, 'core/quartos.html', {'titulo':'Quartos', 'quartos':quartos})


@login_required
def cliente_delete(request, id):
    desabilitar = Hospede.objects.get(id=id)
    desabilitar.habilitado = False
    desabilitar.save()
    return redirect('clientes')

@login_required
def quarto_delete(request, id):
    desabilitar = Quarto.objects.get(id=id)
    desabilitar.habilitado = False
    desabilitar.save()
    return redirect('quartos')


@login_required
def reservar(request):


    quartos = Quarto.objects.filter(habilitado = True, usuario=request.user).order_by('numero')
    return render(request, 'core/reservar.html', {'titulo':'Cadastro de Reserva', 'quartos':quartos})


@login_required
def logout_view(request):
    logout(request)
    return redirect('home')











@login_required
def disponibilidade(request):
    hospedados = Hospedado.objects.filter(usuario=request.user).order_by('data_entrada')

    quarto = request.GET.get('quarto')
    hospede = request.GET.get('hospede')
    checkin = request.GET.get('checkin')  #'2023-02-25 00:00:00+00:00'
    checkout =request.GET.get('checkout')

    if quarto or hospede:# or checkin or checkout:
        hospedados = Hospedado.objects.filter(usuario=request.user, numero_quarto__icontains = quarto, nome_hospede__icontains = hospede).order_by('data_entrada')
        #, data_entrada = checkin, data_saida = checkout )

    for item in hospedados:
        #print(item.data_entrada)
        item.data_entrada = '{}/{}/{}'.format(item.data_entrada.day, item.data_entrada.month,item.data_entrada.year)
        item.data_saida = '{}/{}/{}'.format(item.data_saida.day, item.data_saida.month,item.data_saida.year)
        item.data_reserva = '{}/{}/{}'.format(item.data_reserva.day, item.data_reserva.month,item.data_reserva.year)

    return render(request, 'core/disponibilidade.html', {'titulo':'Reservas Feitas', 'hospedados':hospedados})


