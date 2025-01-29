from factory.django import DjangoModelFactory
from factory import SubFactory
from apps.crops_planted.models import CropsPlantedModel


class CropsPlantedFactory(DjangoModelFactory):
    class Meta:
        model = CropsPlantedModel

    harvest = SubFactory("apps.harvest.factories.HarvestFactory")
    farm = SubFactory("apps.farm.factories.FarmFactory")
    product = "SOJA"
    quantity = 100.00
