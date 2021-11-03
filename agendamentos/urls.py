from django.urls import path
from . import views

urlpatterns = [
    path('agedamentos', views.agendamentos, name='agendamentos'),
    path('cria_agendamento', views.cria_agendamento, name='cria_agendamento'),
    path('cancela_agendamento/<int:agendamento_id>', views.cancela_agendamento, name='cancela_agendamento')
]