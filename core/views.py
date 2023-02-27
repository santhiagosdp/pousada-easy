from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from datetime import datetime,timedelta, date

from .models import Hospedado, Quarto, Hospede,Endereco,Reserva,Hospedes_reserva, Produto, Comanda_consumo, Fechamento_conta,Reserva_pendente

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
def home(request, unknown_path=None):
    if unknown_path is not None:
        # Redireciona o usuário para a página inicial se a URL não existe
        return redirect('home')
    
    
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
        hospede_cad.save()
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
def produtos(request):    
    ##CADASTRO DE QUARTO POST
    if request.method == 'POST':   
        produto_cad = Produto.objects.create(
                usuario = request.user,
                nome = request.POST.get("nome").upper(),
                descricao = request.POST.get("descricao").upper(),
                valor_custo = request.POST.get("valor_custo").replace(",", "."),
                valor_venda = request.POST.get("valor_venda").replace(",", ".")
        )
        produto_cad.save

        return redirect('produtos') 
    #####  FIM DO CADASTRO DO QUARTO


    produtos = Produto.objects.filter(habilitado = True, usuario=request.user).order_by('nome')

    ## botão de buscar hospede get
    buscar = request.GET.get('search')
    if buscar:
        produtos = Produto.objects.filter(habilitado = True, usuario=request.user, nome__icontains = buscar).order_by('nome')
    ####### FIM DO BUSCAR

    return render(request, 'core/produtos.html', {'titulo':'Produtos', 'produtos':produtos})


@login_required
def comandas(request):
    hospedados = Hospedes_reserva.objects.filter(usuario = request.user,
                                                 habilitado = True
                                                 )
    aux = []
    abertos = []
    hoje = date.today() # checkin tem que ser antes e checkout depois
    for item in hospedados:
        if item.reserva.data_entrada < hoje and item.reserva.data_saida > hoje and item.status == "CHECK-IN OK":
            aux.append(item)
            #print (item)
        if item.reserva.data_saida < hoje and item.status == "EM ABERTO":
            abertos.append(item)
    hospedados = aux
    context = {'titulo':'Comandas',
               'hospedados': hospedados,
               'abertos' : abertos }
    return render(request, 'core/comandas.html', context)

@login_required
def itenscomanda(request, id):

    hospede_reserva = Hospedes_reserva.objects.get(id = id,
                                                   usuario = request.user,
                                                   habilitado = True
    )
    
    produtos = Produto.objects.filter(habilitado = True,
                                      usuario = request.user
    )
    
    produtos_comanda = Comanda_consumo.objects.filter(usuario=request.user,
                                                      habilitado = True,
                                                      hospedes_reserva = hospede_reserva
    )
    
    if request.method == 'POST':
        produto = Produto.objects.get(usuario = request.user,
                                      id=request.POST.get("id_produto"),
        )
        quantidade = int(request.POST.get("quantidade"))
        while quantidade>0:
            quantidade = quantidade -1
            produtos_comanda = Comanda_consumo.objects.create(usuario = request.user,
                                                            hospedes_reserva = hospede_reserva,
                                                            produto = produto
            )      
            produtos_comanda.save
            print(produto)

        return redirect('/comanda/hospedagem/'+id)
    
    valor_comanda = 0
    for item in produtos_comanda:
        valor_comanda = valor_comanda + item.produto.valor_venda
    
    produtos_comanda_com_indices = [(i+1, p) for i, p in enumerate(produtos_comanda)]
    context = {'titulo':'Itens da Comanda',
               'hospede_reserva' : hospede_reserva,
               "produtos" : produtos,
               "produtos_comanda" : produtos_comanda_com_indices,
               "valor_comanda" : valor_comanda
               }
    
    return render(request, 'core/itenscomanda.html', context )


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
def produto_delete(request, id):
    desabilitar = Produto.objects.get(id=id)
    desabilitar.habilitado = False
    desabilitar.save()
    return redirect('produtos')

@login_required
def comanda_produto_delete(request, idcomandaconsumo, idhospede):
    desabilitar = Comanda_consumo.objects.get(id=idcomandaconsumo,
                                              usuario = request.user
    )
    desabilitar.habilitado = False
    desabilitar.save()
    return redirect('/comanda/hospedagem/'+idhospede)

@login_required
def hospedagem_checkin(request, id):
    #CHECKIN DO Hospede_Reserva
    hospede_reserva = Hospedes_reserva.objects.get(id=id, usuario = request.user)
    if hospede_reserva.status != "CHECK-IN":
        hospede_reserva.status = 'CHECK-IN'
    else:
        hospede_reserva.status = 'EM ABERTO'
    hospede_reserva.save()

    return redirect('disponibilidade')

@login_required
def hospedagem_delete(request, id):

    #Deletando Hospede_Reserva
    hospede_reserva = Hospedes_reserva.objects.get(id=id, usuario = request.user)
    hospede_reserva.habilitado = False
    hospede_reserva.status = 'DELETADO'
    hospede_reserva.save()

    #Deletando Reserva
    Reserva = hospede_reserva.reserva
    Reserva.habilitado = False
    Reserva.save()

    #deletando as comandas 
    desabilitar = Comanda_consumo.objects.filter(usuario = request.user, hospedes_reserva = hospede_reserva)
    for comanda in desabilitar: 
        comanda.habilitado = False
        comanda.save()
    # deletando os fechamento_conta
    desabilitar = Fechamento_conta.objects.filter(usuario = request.user, hospedes_reserva = hospede_reserva)
    for fechamento in desabilitar: 
        fechamento.habilitado = False
        fechamento.save()
    
    return redirect('disponibilidade')


@login_required
def hospedagem_concluir(request, id):
    #concluindo Hospede_Reserva
    hospede_reserva = Hospedes_reserva.objects.get(id=id, usuario = request.user)
    hospede_reserva.status = 'CHECK-OUT'
    hospede_reserva.save()

    #Deletando Reserva
    Reserva = hospede_reserva.reserva
    Reserva.habilitado = False
    Reserva.save()

    #deletando as comandas 
    desabilitar = Comanda_consumo.objects.filter(usuario = request.user, hospedes_reserva = hospede_reserva)
    for comanda in desabilitar: 
        comanda.habilitado = False
        comanda.save()
    # deletando os fechamento_conta
    #desabilitar = Fechamento_conta.objects.filter(usuario = request.user, hospedes_reserva = hospede_reserva)
    #for fechamento in desabilitar: 
        #fechamento.habilitado = False
        #fechamento.save()
    
    return redirect('disponibilidade')

@login_required
def reservar(request):
    quartos = []
    clientes = Hospede.objects.filter(habilitado = True, usuario=request.user).order_by('nome')
    quartos_disponiveis = []
    quartos_reservados = []
    res_pendente = ""

    ## botão de buscar hospede get
    checkin = request.GET.get('checkin')    
    checkout = request.GET.get('checkout')
    quantidade_hospedes = request.GET.get('quantidade_hospedes')
    id_quarto = request.GET.get('id_quarto')



    if request.method == 'POST':    #### cadastrar a reserva confirmada
        #print("METODO POST")
        #print("#########################POST")
        #print(request.POST.get("valortotal"))
        #print(float(request.POST.get("valortotal")))


        pendente = Reserva_pendente.objects.get(
            usuario = request.user
            )
        quarto = Quarto.objects.get(
            id = request.POST.get("id_quarto"),
            usuario = request.user,
        )
        ## criando reserva confirmada   
        reserva = Reserva.objects.create(
            usuario = request.user,
            quarto = quarto,
            quantidade_hospedes = pendente.quantidade_hospedes,
            data_entrada = pendente.data_entrada,
            data_saida = pendente.data_saida,
            diarias = pendente.diarias,
            valor = float(request.POST.get("valortotal").replace(",", "."))
            )   
        print(reserva)
        reserva.save()
        
        hospede = Hospede.objects.get(
            usuario = request.user,
            id = request.POST.get("cliente")
        )

        hospedes_reserva = Hospedes_reserva.objects.create(
            usuario = request.user,
            hospede = hospede,
            reserva = reserva
        )
        hospedes_reserva.save()

        #apaga as reservas não resolvidas
        pendente = Reserva_pendente.objects.filter(usuario=request.user)
        pendente.delete()
        ###############

        return redirect('disponibilidade') #pagina de confirmação
    


    else:
        if checkin and checkout and quantidade_hospedes:
            checkin = datetime.strptime(checkin, "%Y-%m-%d")
            checkout = datetime.strptime(checkout, "%Y-%m-%d")
            quantidade_hospedes = int(quantidade_hospedes)
            
            #if data checkin menor que checkout
            if checkin < checkout:
                #apaga as reservas não resolvidas
                pendente = Reserva_pendente.objects.filter(usuario=request.user)
                pendente.delete()
                #########               

                quartos = Quarto.objects.filter(habilitado = True, usuario=request.user).order_by('numero') #__icontains
                
                #SEPARAR QUARTOS QUE TEM CAPACIDADE PARA OS HOSPEDES
                for quarto in quartos: 
                    if quarto.capacidade >= quantidade_hospedes:
                        quartos_disponiveis.append(quarto)
                        print(quartos_disponiveis)
                        print("quartos_disponiveis ##########################")
                ##########

                ##DEFINIR ARRAY DE DATAS DA RESERVA_A_CONFIRMAR
                datas_check = [] ## datas da reserva que esta em andamento
                data = checkin
                diarias = 0
                while data < checkout:
                    datas_check.append(data)
                    diarias = diarias+1
                    data = data+timedelta(1)

                reservas = Reserva.objects.filter(habilitado = True, usuario=request.user).order_by('data_entrada')
                for reserva in reservas:
                    reserva.data_entrada = datetime.strptime(str(reserva.data_entrada), "%Y-%m-%d")
                    reserva.data_saida = datetime.strptime(str(reserva.data_saida), "%Y-%m-%d")
                    datas_reserva = []  ## datas da reserva confirmada object
                    data = reserva.data_entrada
                    while data < reserva.data_saida:
                        datas_reserva.append(data)
                        data = data+timedelta(1)
                    print(datas_reserva)
                    print("datas_reserva ##########################")
                    
                    for data in datas_check:
                        for data2 in datas_reserva: 
                            if  data == data2:
                                quartos_reservados.append(reserva.quarto)
                                break
                            #if
                        #for
                    #for
                    print(quartos_reservados)
                    print("quartos_reservados ##########################")

                ## tenho QUARTOS.RESERVADOS e QUARTOS_DISPONIVEIS. 
                ##  FAZER A CONCILIAÇÃO PARA TIRAR OS QUARTOS RESERVADOS DO ARRAY DE QUARTOS DISPONIVEIS
                quartos_final = []
                for quarto1 in quartos_disponiveis:
                    reservado = False
                    for quarto2 in quartos_reservados:
                        if quarto1 == quarto2:
                            reservado = True
                    if reservado == False:
                        quartos_final.append(quarto1)

                print(quartos_final)
                print("quartos_final ##########################")
            ####### FIM DO BUSCAR
                quartos_disponiveis = quartos_final
                ############## criar_reserva_pendente()
                res_pendente = Reserva_pendente.objects.create(
                    usuario=request.user,
                    data_entrada=checkin,
                    data_saida=checkout,
                    quantidade_hospedes=quantidade_hospedes,
                    diarias = diarias
                )
                res_pendente.save()
                ######### fim criar reserva pendente

        else: 
            if id_quarto:  # GET QUARTO 
            
                context = {'clientes':clientes, 'titulo':"Reservar Quarto", "pagina":"dados_reserva"}
                return render(request, 'core/reservar.html', context)   
            
    context = { "clientes":clientes,'titulo':"Reservar Quarto", 'quartos':quartos_disponiveis, "pagina":"quartos","pendente":res_pendente}
    return render(request, 'core/reservar.html', context)


@login_required
def logout_view(request):
    logout(request)
    return redirect('home')



@login_required
def disponibilidade(request):
    hospedados = Hospedes_reserva.objects.filter(usuario = request.user, habilitado = True)
    aux = []
    for item in hospedados:
        if item.status != "CHECK-OUT":
            aux.append(item)
    hospedados = aux
    #######GET DE PESQUISAR FILTRAR
    quarto = request.GET.get('quarto')
    hospede = request.GET.get('hospede')
    checkin = request.GET.get('checkin')  #'2023-02-25 00:00:00+00:00'
    checkout =request.GET.get('checkout')

    if quarto:# or checkin or checkout:
        quarto_pesq = Quarto.objects.filter(habilitado = True, usuario = request.user, numero__icontains = quarto)
        #hospede_pesq = Hospede.objects.filter(usuario = request.user, nome__icontains = hospede)
        pesquisa = []
        for item in hospedados:
            for quarto in quarto_pesq:
                if item.reserva.quarto == quarto:
                    pesquisa.append(item)
        hospedados = pesquisa

    #Se clicar em concluidos
    status = request.GET.get('status')
    if status: # == concluidos
        hospedados = Hospedes_reserva.objects.filter(habilitado = True, usuario=request.user, status="CHECK-OUT")

    ## Definir Valores de comanda e total
    comandas = Comanda_consumo.objects.filter(habilitado = True, usuario = request.user)
    for item in hospedados:
        item.reserva.data_saida = item.reserva.data_saida.strftime('%Y/%m/%d')
        item.reserva.data_entrada = item.reserva.data_entrada.strftime('%Y/%m/%d')
        item.reserva.data_criacao = item.reserva.data_criacao.strftime('%Y/%m/%d')
        for comanda in comandas: 
            if comanda.hospedes_reserva == item:
                item.valor_comanda = item.valor_comanda+comanda.produto.valor_venda
        item.valor_total = item.reserva.valor + item.valor_comanda


    #ordenando pela data de entrada checkin
    hospedados = sorted(hospedados, key=lambda x: x.reserva.data_entrada)
    context = {'titulo' : 'Reservas Feitas',
               'hospedados' : hospedados,
               'hoje': datetime.now().strftime('%Y/%m/%d')
               }
    return render(request, 'core/disponibilidade.html', context)


