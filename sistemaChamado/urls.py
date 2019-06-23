from django.urls import path, include
from  . import views
from django.views.generic import TemplateView

urlpatterns = [
path('', views.index, name='index'),
path('index/', views.index, name='index'),
path('chamados/', views.chamadosRender, name='chamados.html'),
path('atualizar/<int:id>/', views.atualizar, name='atualizar.html'),
path('deletar/<int:id>/', views.deletarChamado, name='deletar.html'),
path('abertos/', views.indexAbertos, name='abertos'),
path('concluidos/', views.indexConcluidos, name='concluidos'),
path('contato/', views.contato, name='contato'),
path('contato/obg', views.obg, name='obg'),
]