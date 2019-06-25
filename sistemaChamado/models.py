from django.db import models
from django.utils import timezone
from django import forms
from django.contrib.auth.models import AbstractUser
from setores.models import Setores, Prioridades


class Chamados(models.Model):
    assunto = models.CharField(max_length=200)
    descricao = models.CharField(max_length=200)
    prioridade = models.ForeignKey(Prioridades, on_delete=models.CASCADE, default=0)
    status = models.CharField(max_length=20, default="Não Realizado", blank=True)
    usuario = models.CharField(max_length=50, default="sem usuario", blank=True)
    setor = models.ForeignKey(Setores, on_delete=models.CASCADE, default=0)
    solucao = models.CharField(max_length=250, default="", blank=True)
    data = models.DateTimeField(default=timezone.now)

    def __str__(self):
    	return self.setor


    
    




    