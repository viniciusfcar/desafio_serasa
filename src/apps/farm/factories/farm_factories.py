from factory.django import DjangoModelFactory
from factory import Faker, SubFactory
from apps.farm.models import FarmModel


class FarmFactory(DjangoModelFactory):
    class Meta:
        model = FarmModel

    farmer = SubFactory("apps.farmer.factories.FarmerFactory")
    name_farm = Faker("name")
    address = SubFactory("apps.address.factories.AddressFarmFactory")
    total_area_farm = 100.00
    agricultural_area = 70.00
    vegetation_area = 30.00
