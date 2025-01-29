from django.db import models
from apps.address.models import AddressFarmerModel
from .services.farmer_service import (
    validate_cpf_cnpj,
    definy_type_document
)


class FarmerModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    name = models.CharField(
        max_length=200,
        null=False,
        blank=False,
        verbose_name="Nome do Agricultor"
    )

    document = models.CharField(
        max_length=200,
        validators=[validate_cpf_cnpj],
        unique=True,
        null=False,
        blank=False,
        verbose_name="CPF/CNPJ"
    )

    type_document = models.CharField(
        max_length=10,
        verbose_name="Tipo do Documento"
    )

    deleted = models.BooleanField(
        default=False
    )

    address = models.ForeignKey(
        AddressFarmerModel,
        on_delete=models.DO_NOTHING,
        related_name='farmer_address',
        blank=False,
        null=False,
        verbose_name="Endereço do Fazendeiro"

    )

    class Meta:
        db_table = "farmer"
        verbose_name = "Fazendeiro"
        verbose_name_plural = "Fazendeiros"

    def __str__(self):
        return f'{self.name}, {self.document}'
    
    def save(self, *args, **kwargs):
        if not self.pk:
            self.type_document = definy_type_document(self.document)

        return super().save(*args, **kwargs)


