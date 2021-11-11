from typing import List
from django.contrib import admin
from .models import Vendas

class ListaVendas(admin.ModelAdmin):
    list_display = ('procedimento', 'cliente', 'valor', 'data_venda', 'hora_venda')
    search_fields = ('procedimento', 'cliente', 'data')

admin.site.register(Vendas, ListaVendas)