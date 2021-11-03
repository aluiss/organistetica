from django.db import models
from clientes.models import Clientes
from procedimentos.models import Procedimento
from locaisAtendimentos.models import LocaisAtendimento

class Agendamento(models.Model):
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    procedimento = models.ForeignKey(Procedimento, on_delete=models.CASCADE)
    local_atendimento = models.ForeignKey(LocaisAtendimento, on_delete=models.CASCADE)
    start = models.DateField()
    hora = models.TimeField()
    cor = models.CharField(max_length=10)
    obs_agenda = models.TextField()
    sessoes = models.IntegerField()
    cancelado = models.BooleanField(default=False)

    def __str__(self):
        return self.cliente.nome
    