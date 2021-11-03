from clientes.admin import ListaClientes
from django.contrib import admin
from .models import Agendamento

class ListaAgendamentos(admin.ModelAdmin):
    list_display = ('cliente', 'start', 'procedimento', 'cancelado')
    list_editable = ('cancelado',)
    search_fields = ('cliente', 'start', 'procedimento')    

admin.site.register(Agendamento, ListaAgendamentos)