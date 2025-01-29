from django.db import models
from apps.farmer.models import FarmerModel
from apps.address.models import AddressFarmModel
from .services.farm_service import validation_total_area


class FarmModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    farmer = models.ForeignKey(
        FarmerModel,
        on_delete=models.DO_NOTHING,
        related_name='farm_farmer',
        blank=False,
        null=False,
        verbose_name="Agricultor"
    )

    name_farm = models.CharField(
        max_length=300,
        null=False,
        blank=False,
        verbose_name="Nome da Fazenda/Propriedade"
    )

    address = models.ForeignKey(
        AddressFarmModel,
        on_delete=models.DO_NOTHING,
        related_name='farm_address',
        blank=False,
        null=False,
        verbose_name="Endereço da Fazenda"
    )

    total_area_farm = models.DecimalField(
        decimal_places=2,
        max_digits=10,
        blank=False,
        null=False,
        verbose_name="Área Total"
    )

    agricultural_area = models.DecimalField(
        decimal_places=2,
        max_digits=10,
        blank=False,
        null=False,
        verbose_name="Área Agricultável"
    )

    vegetation_area = models.DecimalField(
        decimal_places=2,
        max_digits=10,
        blank=False,
        null=False,
        verbose_name="Área de Vegetação"
    )

    class Meta:
        db_table = "farm"
        verbose_name = "Fazenda"
        verbose_name_plural = "Fazendas"

    def __str__(self):
        return f"{self.name_farm} - {self.farmer.name} / {self.farmer.document}"
    
    def save(self, *args, **kwargs):
        if not self.pk:
            validation_total_area(
                self.total_area_farm,
                self.agricultural_area,
                self.vegetation_area
            )

        return super().save(*args, **kwargs)


