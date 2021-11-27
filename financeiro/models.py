from django.db import models
from django.db.models.fields.json import JSONField
from procedimentos.models import Procedimento
from agendamentos.models import Agendamento
from clientes.models import Clientes

class Vendas(models.Model):
    tipo_compra_escolha = [
        ('av', 'À vista'),
        ('pc', 'Parcelado'),
        ('mt', 'Misto'),
    ]
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    procedimento = models.ForeignKey(Procedimento, on_delete=models.CASCADE)
    agendamento = models.ForeignKey(Agendamento, on_delete=models.CASCADE)
    data_venda = models.DateField(auto_now_add=True)    
    hora_venda = models.TimeField(auto_now_add=True)
    tipo_compra = models.CharField(max_length=2, choices=tipo_compra_escolha, default='av')
    data_vencimento = models.DateField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    valor_dinheiro = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    valor_cartao = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    valor_pago = models.DecimalField(max_digits=10, decimal_places=2)
    pago = models.BooleanField(default=False)
    encerrada = models.BooleanField(default=False)

    def __str__(self):
        return self.pk

class Pacotes(models.Model):
    nome = models.TextField(max_length=100, blank=False)
    procedimentos = JSONField()