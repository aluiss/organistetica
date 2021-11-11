from django.contrib import admin
from .models import Procedimento

class ListaProcedimentos(admin.ModelAdmin):
    list_display = ('procedimento', 'valor')
    search_fields = ('procedimento',)

admin.site.register(Procedimento, ListaProcedimentos)