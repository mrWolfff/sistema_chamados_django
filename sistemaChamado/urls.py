from django.urls import path, include
from  . import views

urlpatterns = [
path('index/', views.index, name='index.html'),
path('chamados/', views.chamadosRender, name='chamados.html'),
path('atualizar/<int:id>/', views.atualizar, name='atualizar.html'),
path('deletar/<int:id>/', views.deletarChamado, name='deletar.html'),
path('filtrar/', views.filtrar, name='filtrar.html'),
]