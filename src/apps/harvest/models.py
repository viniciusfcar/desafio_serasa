from django.db import models


class HarvestModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    name = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        verbose_name="Nome da Safra"
    )

    year = models.CharField(
        max_length=4,
        null=False,
        blank=False,
        verbose_name="Ano da Safra"
    )

    class Meta:
        db_table = "harvest"
        verbose_name = "Safra"
        verbose_name_plural = "Safras"

    def __str__(self):
        return f"{self.name} - {self.year}"
