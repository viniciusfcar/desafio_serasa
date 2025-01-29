from factory.django import DjangoModelFactory
from factory import Faker
from apps.address.models import AddressFarmerModel


class AddressFarmerFactory(DjangoModelFactory):
    class Meta:
        model = AddressFarmerModel

    city = Faker("city")
    complement = Faker("secondary_address")
    country = Faker("country")
    neighborhood = Faker("sentence", nb_words=3)
    number = Faker("building_number")
    state = Faker("state")
    street = Faker("street_address")
    postal_code = Faker("postcode", locale="pt-BR")
