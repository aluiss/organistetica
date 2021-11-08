from django.urls import path
from . import views

urlpatterns = [
    path('agedamentos', views.agendamentos, name='agendamentos'),
    path('cria_agendamento', views.cria_agendamento, name='cria_agendamento'),
    path('cancela_agendamento/<int:agendamento_id>', views.cancela_agendamento, name='cancela_agendamento'),
    path('altera_agendamento/<int:agendamento_id>', views.altera_agendamento, name='altera_agendamento'),
    path('atualiza_agendamento', views.atualiza_agendamento, name='atualiza_agendamento')
]