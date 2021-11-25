from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Count
from .models import Clientes
from agendamentos.models import Agendamento
from datetime import date
from django.core.paginator import Paginator

def index(request):
    #lista todos os clientes por ordem de cadastro
    lista_clientes = Clientes.objects.all()
    #lista os agendamentos que não foram cancelados em ordem decrescente
    lista_agendamentos = Agendamento.objects.filter(cancelado=False).order_by('-start')

    #Lista os clientes que têm agendamentos e o total de agendamentos de cada um deles
    conta_agendamentos = Agendamento.objects.values('cliente__nome').annotate(Count('id'))
    conta_agendamentos = conta_agendamentos.order_by('-id__count')
    #lista os clientes em ordem aleatória
    clientes_aleatorios = lista_clientes.order_by('?')

    if 'pesquisa_agendamentos' in request.GET:
        agendamento_a_pesquisar = request.GET['pesquisa_agendamentos']
        if index:
            lista_agendamentos = lista_agendamentos.filter(cliente__nome__icontains=agendamento_a_pesquisar)

    #Paginação
    paginator = Paginator(lista_agendamentos, 9)
    page = request.GET.get('page')
    agendamentos_por_pagina = paginator.get_page(page)

    #Conta total de clientes
    total_de_clientes = lista_clientes.values('id').count()
    
    class Agendamentos():
        def agendamentosHoje():
            agendamentos_hoje = Agendamento.objects.filter(start=date.today(), cancelado=False).count()
            if agendamentos_hoje == "":
                return "0"
            else:
                return agendamentos_hoje
        
        def agendamentosMes():
            mes_atual = date.today().month
            agendamentos_mes = Agendamento.objects.filter(start__month=mes_atual)

            if agendamentos_mes == "":
                return "0"
            else:
                return agendamentos_mes.count()

        def agendamentosCancelados():
            agendamentos_cancelados = Agendamento.objects.filter(cancelado=True).count()
            if agendamentos_cancelados == "":
                return "0"
            else:
                return agendamentos_cancelados
        
        def vagas_hoje():
            hoje = date.today().day
            vagas_hoje = 10 - Agendamento.objects.filter(start__day=hoje, cancelado=False).count()
            return vagas_hoje

    dados = {
        'clientes' : lista_clientes,
        'dados' : agendamentos_por_pagina,
        'agendamentos' : lista_agendamentos,
        'cli_aleatorios' : clientes_aleatorios,
        'conta_agendamentos' : conta_agendamentos,
        'total_clientes' : total_de_clientes,
        'agendamentos_hoje' : Agendamentos.agendamentosHoje,
        'agendamentos_mes' : Agendamentos.agendamentosMes,
        'agendamentos_cancelados' : Agendamentos.agendamentosCancelados,
        'vagas_hoje' : Agendamentos.vagas_hoje,
    }
    return render(request, 'index.html', dados)

def clientes(request):
    clientes = Clientes.objects.all().order_by('nome')

    #Configuração da paginação da lista de clientes
    paginator = Paginator(clientes, 12)
    page = request.GET.get('page')
    clientes_por_pagina = paginator.get_page(page)
    
    #Pesquisa de clientes
    if 'pesquisa_clientes' in request.GET:
        cliente_pesquisado = request.GET['pesquisa_clientes']
        if 'clientes':
            clientes_por_pagina = clientes.filter(nome__icontains=cliente_pesquisado)
    dados = {
        'dados' : clientes_por_pagina,
    }
    return render(request, 'clientes.html', dados)

def cadastra_cliente(request):
    #Armazena as informações do form em variáveis
    if request.method == 'POST':
        nome = request.POST['nome']
        telefone = request.POST['telefone']
        email = request.POST['email']
        rg = request.POST['rg']
        cpf = request.POST['cpf']
        sexo = request.POST['sexo']
        estado_civil = request.POST['estado_civil']
        nascimento = request.POST['nascimento']
        endereco = request.POST['endereco']
        cep = request.POST['cep']
        obs = request.POST['observacao']
        #Verifica se o sexo é masculino para trocar o estado civil
        if request.POST['sexo'] == 'ms' and request.POST['estado_civil'] == 'sta':
            estado_civil = 'st'
        elif request.POST['sexo'] == 'ms' and request.POST['estado_civil'] == 'csa':
            estado_civil = 'cs'
        elif request.POST['sexo'] == 'ms' and request.POST['estado_civil'] == 'dva':
            estado_civil = 'dv'
        elif request.POST['sexo'] == 'ms' and request.POST['estado_civil'] == 'vva':
            estado_civil = 'vv'
        #Verificar se foi selecionada uma foto para upload
        if not request.FILES:
            foto = 'perfil.png'
        else:
            foto = request.FILES['foto']
        #Verificar se os campos estão preenchidos.
        if campo_vazio(nome):
            messages.error(request, 'O campo de nome está em branco.')
            return redirect('clientes')
        if campo_vazio(nascimento):
            messages.error(request, 'Favor digitar a data de nascimento da(o) cliente!')
            return redirect('clientes')
        if not rg:
            messages.error(request, 'Favor digitar o RG da(o) cliente!')
            return redirect('clientes')
        if not cpf:
            messages.erro(request, 'Favor digitar o CPF da(o) cliente!')
            return redirect('clientes')
        if campo_vazio(endereco):
            messages.error(request, 'Favor digitar o endereço da(o) cliente!')
            return redirect('clientes')
        if Clientes.objects.filter(nome=nome).exists():
            messages.error(request, 'Já existe uma(um) cliente com o nome, ' + nome + ', cadastrada(o).')
            return redirect('clientes')
        #cria um objeto 'cliente' contendo os dados recuperados do formulário
        cliente = Clientes.objects.create(
            nome = nome,
            telefone = telefone,
            email = email,
            data_nascimento = nascimento,
            rg = troca_sinal(rg),
            cpf = troca_sinal(cpf),
            sexo = sexo,
            estado_civil = estado_civil,
            endereco = endereco,
            cep = cep,
            obs = obs,
            foto = foto
        )
        #salva o novo cliente no banco de dados
        cliente.save()
        messages.success(request, nome +', cadastrada(o) com sucesso!')
        #Redireciona para a página 'clientes'
        return redirect('clientes')
    #Renderiza a página de clientes
    return render(request, 'cliente/cadastra_cliente.html')

def deleta_cliente(request, cliente_id):
    cliente = get_object_or_404(Clientes, pk=cliente_id)
    cliente.delete()
    messages.error(request, 'Cliente apagada(o).')
    return redirect('clientes')

def edita_cliente(request, cliente_id):
    cliente = get_object_or_404(Clientes, pk=cliente_id)
    dados_cliente = {'cliente': cliente}
    return render(request, 'cliente/edita_cliente.html', dados_cliente)

def atualiza_cliente(request):
    if request.method == 'POST':
        id_cliente = request.POST['id_cliente']
        cli = Clientes.objects.get(pk=id_cliente)
        cli.nome = request.POST['nome']
        cli.email = request.POST['email']
        cli.telefone = request.POST['telefone']
        cli.rg = troca_sinal(request.POST['rg'])
        cli.cpf = troca_sinal(request.POST['cpf'])
        if 'nascimento' in request.POST:
            cli.data_nascimento = request.POST['nascimento']
        else:
            cli.data_nascimento = cli.data_nascimento
        cli.endereco = request.POST['endereco']
        cli.cep = request.POST['cep']
        cli.sexo = request.POST['sexo']
        cli.obs = request.POST['observacao']
        if 'foto' in request.FILES:
            cli.foto = request.FILES['foto']
        if request.POST['sexo'] == 'ms' and request.POST['estado_civil'] == 'sta':
            cli.estado_civil = 'st'
        elif request.POST['sexo'] == 'ms' and request.POST['estado_civil'] == 'csa':
            cli.estado_civil = 'cs'
        elif request.POST['sexo'] == 'ms' and request.POST['estado_civil'] == 'dva':
            cli.estado_civil = 'dv'
        elif request.POST['sexo'] == 'ms' and request.POST['estado_civil'] == 'vva':
            cli.estado_civil = 'vv'
        cli.save()
    messages.success(request, 'Cliente ' + cli.nome + ' alterada(o) com sucesso!')
    return redirect('clientes')

#Verifica se um determinado campo está vazio
def campo_vazio(campo):
    return not campo.strip()

#Troca os sinais ',' (vírgula) por '.' (ponto).
def troca_sinal(valor):
    return str(valor).replace(',','.')