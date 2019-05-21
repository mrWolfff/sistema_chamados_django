from django.db import models
from django.utils import timezone
from django import forms
from django.contrib.auth.models import AbstractUser
from django.db import models


class Chamados(models.Model):
    assunto = models.CharField(max_length=200)
    descricao = models.CharField(max_length=200)
    prioridade = models.CharField(max_length=200)
    status = models.CharField(max_length=20, default="Não Realizado", blank=True)
    usuario = models.CharField(max_length=50, default="admin", blank=True)
    solucao = models.CharField(max_length=250, default="", blank=True)
    data = models.DateTimeField(default=timezone.now)



class Usuarios(models.Model):
	nome = models.CharField(max_length=200)
	senha = forms.CharField(widget=forms.PasswordInput)
	email = models.CharField(max_length=200)
	admin = models.CharField(max_length=10, default="off", blank=True)



    