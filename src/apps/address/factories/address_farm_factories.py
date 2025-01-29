from factory.django import DjangoModelFactory
from factory import Faker
from apps.address.models import AddressFarmModel


class AddressFarmFactory(DjangoModelFactory):
    class Meta:
        model = AddressFarmModel

    city = Faker("city")
    state = Faker("state")
    postal_code = Faker("postcode", locale="pt-BR")
