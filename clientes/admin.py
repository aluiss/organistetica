from django.contrib import admin
from .models import Clientes

class ListaClientes(admin.ModelAdmin):
    list_display = ('nome', 'data_nascimento', 'endereco')
    search_fields = ('nome', 'endereco')

admin.site.register(Clientes, ListaClientes)