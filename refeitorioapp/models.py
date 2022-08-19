from django.db import models
from PIL import Image

# Create your models here.
class Mesa(models.Model):
    nome = models.CharField(max_length=200)
    capacidade = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    foto = models.ImageField(blank=True, null=True)
    