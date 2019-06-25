from django.db import models
from django.contrib.auth.models import AbstractUser
from setores.models import Setores

class CustomUser(AbstractUser):
	# add additional fields in here
    imagem = models.ImageField(upload_to='../media', null=True, blank=True)
    setor = models.ForeignKey(Setores, on_delete=models.CASCADE, default=0)

    def __str__(self):
        return self.email