from django.db import models

from core.models import Modelo, Cor, Acessorio

class Veiculo(models.Model):
    modelo = models.ForeignKey( Modelo, on_delete=models.RESTRICT)
    cor =  models.ForeignKey( Cor , on_delete=models.RESTRICT)
    ano = models.DecimalField(max_digits=4, decimal_places=0)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    acessorios = models.ForeignKey( Acessorio, on_delete=models.RESTRICT)

    def __str__(self):
        return f"{self.modelo}"

    class Meta:
        verbose_name = "Veículo"
        verbose_name_plural = "Veículos"