from django.urls import path, include
from  . import views

urlpatterns = [
path('setores/', views.setores, name='setores'),
path('novosetor/', views.novoSetor, name='novosetor'),
path('setor/<int:id>/', views.setor, name='setor')
]