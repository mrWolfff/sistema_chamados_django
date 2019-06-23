from django.db import models
from django.utils import timezone
from django import forms
from django.contrib.auth.models import AbstractUser


class Chamados(models.Model):
    assunto = models.CharField(max_length=200)
    descricao = models.CharField(max_length=200)
    prioridade = models.CharField(max_length=200)
    status = models.CharField(max_length=20, default="Não Realizado", blank=True)
    usuario = models.CharField(max_length=50, default="sem usuario", blank=True)
    setor = models.CharField(max_length=100, default="None")
    anexo = models.FileField(upload_to='files/', blank=True, default=None)
    solucao = models.CharField(max_length=250, default="", blank=True)
    data = models.DateTimeField(default=timezone.now)
    para_usuario = models.CharField(max_length=50, default="admin")
    cont = models.CharField(max_length=50, default=0)

    def cont(self):
    	chamados = Chamados.objects.all()
    	for chamado in chamados:
    		if chamado.para_usuario == user.username:
    			cont = cont + 1
    	return self.cont


    
    



    