from django.contrib import messages
from django.contrib.messages.api import error
from django.shortcuts import get_object_or_404, render, redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
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

        if campo_vazio(data):
            messages.error(request, 'Não foi definida uma data para o agendamento.')
            return redirect('cria_agendamento')
        
        if campo_vazio(hora):
            messages.error(request, 'Não foi definido um horário para o agendamento.')
            return redirect('cria_agendamento')
        
        if campo_vazio(sessoes):
            messages,error(request, 'O atendimento terá quantas seções?')
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
        'locais' : localatendimento
    }
    return render(request, 'agendamentos/cria_agendamento.html', dados)

#Verifica se um determinado campo está vazio
def campo_vazio(campo):
    return not campo.strip()

def cancela_agendamento(request, agendamento_id):
    agendamento = get_object_or_404(Agendamento, pk=agendamento_id)
    agendamento.cancelado = True
    agendamento.save()
    messages.success(request, 'Agendamento cancelado!')
    return redirect('agendamentos')