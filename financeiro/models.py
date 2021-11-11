from django.db import models
from procedimentos.models import Procedimento
from agendamentos.models import Agendamento

class Vendas(models.Model):
    procedimento = models.ForeignKey(Procedimento, on_delete=models.CASCADE)
    agendamento = models.ForeignKey(Agendamento, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=10 ,decimal_places=2)
    cliente = models.TextField()
    data_venda = models.DateField(auto_now_add=True)
    hora_venda = models.TimeField(auto_now_add=True)
    pago = models.BooleanField(default=False)

    def __str__(self):
        return self.procedimento.procedimento
