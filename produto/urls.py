from django.urls import path

from produto import admin
from . import views

urlpatterns = [

  
  path('', views.salvar_contato, name='salvar_contato'),
  path('listar_contatos/', views.listar_contatos, name='listar_contatos'),
  
     
]

