from factory.django import DjangoModelFactory
from factory import Faker
from apps.harvest.models import HarvestModel


class HarvestFactory(DjangoModelFactory):
    class Meta:
        model = HarvestModel

    name = Faker("name")
    year = Faker("year")
