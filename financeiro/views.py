from django.db.models.aggregates import Sum
from django.shortcuts import render
from procedimentos.models import Procedimento
from .models import Vendas
from datetime import date

def financeiro(request):
    procedimentos = Procedimento.objects.all().order_by('procedimento')
    vendas_servicos_mes = vendasServicoMes()
    vendas_mes = vendasMes()
    vendas_ano = vendasAno()
    dados = {
        'procedimentos' : procedimentos,
        'vendas_serv_mes' : vendas_servicos_mes,
        'vendas_mes' : vendas_mes,
        'vendas_ano' : vendas_ano,
    }
    return render(request, 'financeiro/financeiro.html', dados)

def mesAtual():
    return date.today().month
def anoAtual():
    return date.today().year

def vendasServicoMes():
    vendas = Vendas.objects.values('procedimento__procedimento').annotate(Sum('valor')).filter(data_venda__month=mesAtual()).order_by('-valor__sum')
    return vendas

def vendasMes():
    vendas = Vendas.objects.all().filter(data_venda__month=mesAtual()).aggregate(Sum('valor'))
    return vendas

def vendasAno():
    vendas = Vendas.objects.all().filter(data_venda__year=anoAtual()).aggregate(Sum('valor'))
    return vendas