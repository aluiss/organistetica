from django.db.models.aggregates import Sum
from django.shortcuts import render
from procedimentos.models import Procedimento
from .models import Vendas
from datetime import date

def financeiro(request):
    procedimentos = Procedimento.objects.all().order_by('procedimento')
    vendas_servicos_mes = vendasServicoMes()
    vendas_mes_recebidas = vendasMesRecebido()
    vendas_mes_a_receber = vendasMesAReceber()
    vendas_ano_recebidas = vendasAnoRecebido()
    vendas_ano_a_receber = vendasAnoAReceber()
    dados = {
        'procedimentos' : procedimentos,
        'vendas_serv_mes' : vendas_servicos_mes,
        'vendas_mes_recebidas' : vendas_mes_recebidas,
        'vendas_mes_a_receber' : vendas_mes_a_receber,
        'vendas_ano_recebidas' : vendas_ano_recebidas,
        'vendas_ano_a_receber' : vendas_ano_a_receber
    }
    return render(request, 'financeiro/financeiro.html', dados)

def mesAtual():
    return date.today().month
def anoAtual():
    return date.today().year
def vendasServicoMes():
    vendas = Vendas.objects.values('procedimento__procedimento').annotate(Sum('valor')).filter(data_venda__month=mesAtual()).order_by('-valor__sum')
    return vendas
def vendasMesRecebido():
    vendas = Vendas.objects.all().filter(pago=True, data_venda__month=mesAtual()).aggregate(Sum('valor'))
    return vendas
def vendasMesAReceber():
    vendas = Vendas.objects.all().filter(pago=False, data_venda__month=mesAtual()).aggregate(Sum('valor'))
    return vendas
def vendasAnoRecebido():
    vendas = Vendas.objects.all().filter(pago=True, data_venda__year=anoAtual()).aggregate(Sum('valor'))
    return vendas
def vendasAnoAReceber():
    vendas = Vendas.objects.all().filter(pago=False, data_venda__year=anoAtual()).aggregate(Sum('valor'))
    return vendas