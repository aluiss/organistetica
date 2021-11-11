from django.db.models.aggregates import Sum
from django.shortcuts import render
from procedimentos.models import Procedimento
from .models import Vendas
from datetime import date

def financeiro(request):
    procedimentos = Procedimento.objects.all().order_by('procedimento')
    vendas_mes = vendasMes()
    dados = {
        'procedimentos' : procedimentos,
        'vendas' : vendas_mes,
    }
    return render(request, 'financeiro/financeiro.html', dados)

def vendasMes():
    mes_atual = date.today().month
    vendas = Vendas.objects.values('procedimento').aggregate(Sum('valor'))
    #mes_venda = Vendas.objects.values('data_venda__month')
    #soma_vendas = Vendas.objects.aggregate(Sum('valor'))
    """ if vendas.data_venda__month == mes_atual:
        return vendas #soma_vendas
    else:
        return ('Nenhuma venda realizada.') """
    return vendas