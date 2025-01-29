import pytest
from faker import Faker
import random
from address.factories import (
    AddressFarmFactory,
    AddressFarmerFactory
)


@pytest.fixture
def fake():
    return Faker("pt_BR")


@pytest.fixture
def address_farmer():
    return AddressFarmerFactory()


@pytest.fixture
def address_farm():
    return AddressFarmFactory()


@pytest.fixture
def address_farmer_list(fake):
    return [
        {
            "id": random.randint(1, 100000),
            "created_at": fake.iso8601(),
            "updated_at": fake.iso8601(),
            "postal_code": fake.postcode(),
            "street": fake.street_name(),
            "number": "10",
            "complement": "",
            "neighborhood": fake.city_suffix(),
            "city": fake.city(),
            "state": fake.estado_sigla(),
            "country": "Brazil"
        }
    ]


@pytest.fixture
def address_farmer_object(fake):
    return {
        "postal_code": fake.postcode(),
        "street": fake.street_name(),
        "number": "10",
        "complement": "",
        "neighborhood": fake.city_suffix(),
        "city": fake.city(),
        "state": fake.estado_sigla(),
        "country": "Brazil"
    }


@pytest.fixture
def address_farm_list(fake):
    return [
        {
            "id": random.randint(1, 100000),
            "created_at": fake.iso8601(),
            "updated_at": fake.iso8601(),
            "postal_code": fake.postcode(),
            "city": fake.city(),
            "state": fake.estado_sigla(),
        }
    ]


@pytest.fixture
def address_farm_object(fake):
    return {
        "postal_code": fake.postcode(),
        "city": fake.city(),
        "state": fake.estado_sigla()
    }
