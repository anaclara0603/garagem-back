from django.db import models
from core.models import Categoria, Marca

class Modelo(models.Model):
    nome = models.CharField(max_length=100)
    marca = models.ForeignKey( Marca, on_delete=models.RESTRICT)
    categoria = models.ForeignKey( Categoria, on_delete=models.RESTRICT)

    def __str__(self):
        return f"{self.nome}"

    class Meta:
        verbose_name = "modelo"
        verbose_name_plural = "modelos"