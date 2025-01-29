from django.db import models
from apps.harvest.models import HarvestModel
from apps.farm.models import FarmModel


class ProductPlanted(models.TextChoices):
    SOJA = "soja", "Soja"
    CAFE = "cafe", "Café"
    CANA_DE_ACUCAR = "cana_de_acucar", "Cana-de-açúcar"
    ARROZ = "arroz", "Arroz"
    MILHO = "milho", "Milho"


class CropsPlantedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    harvest = models.ForeignKey(
        HarvestModel,
        on_delete=models.DO_NOTHING,
        related_name='crops_planted_harvest',
        blank=False,
        null=False,
        verbose_name="Safra"
    )

    farm = models.ForeignKey(
        FarmModel,
        on_delete=models.DO_NOTHING,
        related_name='crops_planted_farm',
        blank=False,
        null=False,
        verbose_name="Fazenda"
    )

    product = models.CharField(
        max_length=20,
        choices=ProductPlanted.choices,
        default=ProductPlanted.SOJA,
        blank=False,
        null=False,
        verbose_name="Produto"
    )

    quantity = models.DecimalField(
        decimal_places=2,
        max_digits=10,
        blank=False,
        null=False,
        verbose_name="Quantidade"
    )

    class Meta:
        db_table = "crops_planted"
        verbose_name = "Cultura Plantada"
        verbose_name_plural = "Culturas Plantadas"

    def __str__(self):
        return f"{self.product} - {self.quantity} / {self.farm.name_farm}"
