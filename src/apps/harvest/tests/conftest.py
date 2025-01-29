import pytest
from faker import Faker
import random
from harvest.factories import HarvestFactory


@pytest.fixture
def fake():
    return Faker("pt_BR")


@pytest.fixture
def harvest():
    return HarvestFactory()


@pytest.fixture
def harvest_list(fake):
    return [
        {
            "id": random.randint(1, 100000),
            "created_at": fake.iso8601(),
            "updated_at": fake.iso8601(),
            "name": fake.name(),
            "year": fake.year(),
        }
    ]


@pytest.fixture
def harvest_object(fake):
    return {
        "name": fake.name(),
        "year": fake.year(),
    }
