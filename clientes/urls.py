from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cliente', views.clientes, name='clientes'),
    path('cadastra_cliente', views.cadastra_cliente, name='cadastra_cliente'),
    path('deleta/<int:cliente_id>', views.deleta_cliente, name='deleta_cliente'),
    path('edita_cliente/<int:cliente_id>', views.edita_cliente, name='edita_cliente'),
    path('atualiza_cliente', views.atualiza_cliente, name='atualiza_cliente')
]