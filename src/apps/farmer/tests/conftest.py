import pytest
from faker import Faker
import random
from farmer.factories import FarmerFactory
from apps.address.tests.conftest import address_farmer


@pytest.fixture
def fake():
    return Faker("pt_BR")


@pytest.fixture
def farmer():
    return FarmerFactory()


@pytest.fixture
def farmer_list(fake, address_farmer):
    return [
        {
            "id": random.randint(1, 100000),
            "created_at": fake.iso8601(),
            "updated_at": fake.iso8601(),
            "name": fake.name(),
            "document": fake.ssn(),
            "type_document": "CPF",
            "deleted": False,
            "address": address_farmer.id
        }
    ]


@pytest.fixture
def farmer_object(fake, address_farmer):
    return {
        "name": fake.name(),
        "document": fake.ssn(),
        "type_document": "CPF",
        "deleted": False,
        "address": address_farmer.id
    }
