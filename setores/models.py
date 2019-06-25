from django.db import models
from django.utils import timezone
from django import forms


class Setores(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.CharField(max_length=200)
    telefone = models.CharField(max_length=20)
    data = models.DateTimeField(default=timezone.now)

    def __str__(self):
    	return self.nome

class Prioridades(models.Model):
	nome = models.CharField(max_length=100)

	def __str__(self):
		return self.nome
