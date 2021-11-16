from django.db import models
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
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_venda = models.DateField(auto_now_add=True)    
    hora_venda = models.TimeField(auto_now_add=True)
    data_vencimento = models.DateField()
    pago = models.BooleanField(default=False)
    tipo_compra = models.CharField(max_length=2, choices=tipo_compra_escolha, default='av')

    def __str__(self):
        return self.procedimento.procedimento
