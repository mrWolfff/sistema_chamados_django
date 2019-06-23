from django.db import models
from django.utils import timezone
from django import forms


class Setores(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.CharField(max_length=200)
    telefone = models.CharField(max_length=20)
    data = models.DateTimeField(default=timezone.now)
