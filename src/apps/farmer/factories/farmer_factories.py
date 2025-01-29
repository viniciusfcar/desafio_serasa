from factory.django import DjangoModelFactory
from factory import Faker, SubFactory
from apps.farmer.models import FarmerModel


class FarmerFactory(DjangoModelFactory):
    class Meta:
        model = FarmerModel

    name = Faker("name")
    document = Faker("ssn")
    type_document = "CPF"
    deleted = False
    address = SubFactory("apps.address.factories.AddressFarmerFactory")
