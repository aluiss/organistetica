from django.shortcuts import render
from procedimentos.models import Procedimento

def financeiro(request):
    procedimentos = Procedimento.objects.all().order_by('procedimento')
    dados = {
        'procedimentos' : procedimentos,
    }
    return render(request, 'financeiro/financeiro.html', dados)