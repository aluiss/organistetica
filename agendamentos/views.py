from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect
from django.core.paginator import Paginator
from datetime import datetime
from .models import Agendamento
from .models import Clientes
from .models import LocaisAtendimento
from .models import Procedimento

def agendamentos(request):
    agendamentos = Agendamento.objects.select_related('cliente').order_by('-start')
    #Paginação
    paginator = Paginator(agendamentos, 12)
    page = request.GET.get('page')
    agendamentos_por_pagina = paginator.get_page(page)

    #Pesquisa
    if 'pesquisa_agendamento' in request.GET:
        agendamento_a_pesquisar = request.GET['pesquisa_agendamento']
        if 'agendamentos':
            agendamentos_por_pagina = agendamentos.filter(cliente__nome__icontains=agendamento_a_pesquisar)

    dados = {
        'dados': agendamentos_por_pagina,
    }
    return render(request, 'agendamentos/agendamentos.html', dados)

def cria_agendamento(request):
    clientes = Clientes.objects.all()
    procedimentos = Procedimento.objects.all()
    localatendimento = LocaisAtendimento.objects.all()

    if request.method == 'POST':
        cliente = request.POST['cliente']
        cor = request.POST['cor']
        procedimento = request.POST['procedimento']
        local = request.POST['local']
        data = request.POST['data']
        hora = request.POST['hora']
        sessoes = request.POST['sessoes']
        obs = request.POST['observacao']

        if Agendamento.objects.filter(start=data, hora=hora).exists():
            messages.error(request, 'Já existe um agendamento neste dia e horário.')
            return redirect('cria_agendamento')

        if verifica_select_invalido(cliente):
            messages.error(request, 'Selecione o cliente que será atendido, por favor!')
            return redirect('cria_agendamento')
        
        if verifica_select_invalido(procedimento):
            messages.error(request, 'Selecione o procedimento que será executado.')
            return redirect('cria_agendamento')
        
        if verifica_select_invalido(local):
            messages.error(request, 'Selecione o local do atendimento.')
            return redirect('cria_agendamento')

        if verifica_data_antiga(data, hora):
            messages.error(request, 'Não pode agendar para um dia ou horário anterior a agora.')
            return redirect('cria_agendamento')

        if campo_vazio(data):
            messages.error(request, 'Não foi definida uma data para o agendamento.')
            return redirect('cria_agendamento')
        
        if campo_vazio(hora):
            messages.error(request, 'Não foi definido um horário para o agendamento.')
            return redirect('cria_agendamento')

        if campo_vazio(sessoes):
            messages.error(request, 'O atendimento terá quantas seções?')
            return redirect('cria_agendamento')

        agendamento = Agendamento.objects.create(
            cliente_id = cliente,
            cor = cor,
            procedimento_id = procedimento,
            local_atendimento_id = local,
            start = data,
            hora = hora,
            sessoes = sessoes,
            obs_agenda = obs
        )
        agendamento.save()
        messages.success(request, 'Agendamento realizado!')
    
    dados = {
        'clientes' : clientes,
        'procedimentos' : procedimentos,
        'locais' : localatendimento,
    }
    return render(request, 'agendamentos/cria_agendamento.html', dados)

#Verifica se um determinado campo está vazio
def campo_vazio(campo):
    return not campo.strip()
#Verifica se um select está com a opção 'Selecione..' selecionada
def verifica_select_invalido(select):
    if select == 'Selecione...':
        return True
#Verifica se a data de agendamento é anterior a data e hora atual.
def verifica_data_antiga(data, hora):
    if data and hora:
        data_hora = datetime.strptime(data + ' ' + hora + ':00', '%Y-%m-%d %H:%M:%S')
        hoje = datetime.now()
        
        if hoje > data_hora:
            return True
        return False

def altera_agendamento(request, agendamento_id):
    clientes = Clientes.objects.all()
    procedimentos = Procedimento.objects.all()
    locais = LocaisAtendimento.objects.all()
    agendamentos = Agendamento.objects.filter(pk=agendamento_id)
    dados = {
        'agendamentos' : agendamentos,
        'clientes' : clientes,
        'procedimentos' : procedimentos,
        'locais_atendimento' : locais
        }
    return render(request, 'agendamentos/altera_agendamento.html', dados)

def atualiza_agendamento(request):
    cliente_id = Clientes.objects.values("id").filter(nome=request.POST['cliente'])
    procedimento_id = Procedimento.objects.values("id").filter(procedimento=request.POST['procedimento'])
    local_id = LocaisAtendimento.objects.values("id").filter(local=request.POST['local'])

    if not cliente_id.exists():
        messages.error(request, 'Cliente não encontrado.')
    if not procedimento_id.exists():
        messages.error(request, 'Procedimento não cadastrado.')
    if not local_id.exists():
        messages.error(request, 'Local não cadastrado.')
    if request.method == 'POST':
        agendamento_id = request.POST['id_agendamento']
        agendamento = Agendamento.objects.get(pk=agendamento_id)
        agendamento.cliente_id = cliente_id
        agendamento.cor = request.POST['cor']
        agendamento.procedimento_id = procedimento_id
        agendamento.local_atendimento_id = local_id
        agendamento.start = request.POST['data']
        agendamento.hora = request.POST['hora']
        agendamento.sessoes = request.POST['sessoes']
        agendamento.obs_agenda = request.POST['observacao']
        agendamento.save()

    messages.success(request, 'Agendamento alterado!')
    return redirect('agendamentos')

def cancela_agendamento(request, agendamento_id):
    agendamento = get_object_or_404(Agendamento, pk=agendamento_id)
    agendamento.cancelado = True
    agendamento.save()
    messages.success(request, 'Agendamento cancelado!')
    return redirect('agendamentos')