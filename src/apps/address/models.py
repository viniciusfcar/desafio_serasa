from django.db import models


class AddressFarmerModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    postal_code = models.CharField(
        max_length=10
    )

    street = models.CharField(
        max_length=255
    )

    number = models.CharField(
        max_length=10,
        blank=True,
        null=True
    )

    complement = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

    neighborhood = models.CharField(
        max_length=100
    )

    city = models.CharField(
        max_length=100
    )

    state = models.CharField(
        max_length=2
    )

    country = models.CharField(
        max_length=100,
        default="Brazil"
    )

    class Meta:
        db_table = "address_farmer"
        verbose_name = "Endereço do Fazendeiro"
        verbose_name_plural = "Endereços dos Fazendeiros"

    def __str__(self):
        return f"{self.street}, {self.neighborhood} - {self.city}/{self.state}"
    

class AddressFarmModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    postal_code = models.CharField(
        max_length=10
    )

    city = models.CharField(
        max_length=100
    )

    state = models.CharField(
        max_length=2
    )

    class Meta:
        db_table = "address_farm"
        verbose_name = "Endereço da Fazenda"
        verbose_name_plural = "Endereços das Fazendas"

    def __str__(self):
        return f"{self.city}/{self.state} - Postal Code: {self.postal_code}"
