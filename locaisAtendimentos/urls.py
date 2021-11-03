from django.urls import path
from . import views

urlpatterns = [
    path('locaisAtendimentos', views.locaisAtendimentos, name='locaisAtendimentos'),
]