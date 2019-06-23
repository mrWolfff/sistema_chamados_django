from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
	# add additional fields in here
    imagem = models.ImageField(upload_to='../media', null=True, blank=True)
    setor = models.CharField(max_length=50, default="Sem setor", null=True)

    def __str__(self):
        return self.email