from django import template
from datetime import date

register = template.Library()

@register.simple_tag
def calcula_idade(nascimento):
    hoje = date.today()
    idade = hoje.year - nascimento.year - ((hoje.month, hoje.day) < (nascimento.month, nascimento.day))
    return idade