import pytest
from faker import Faker
import random
from crops_planted.factories import CropsPlantedFactory
from apps.harvest.tests.conftest import harvest
from apps.farm.tests.conftest import farm


@pytest.fixture
def fake():
    return Faker("pt_BR")


@pytest.fixture
def crops_planted():
    return CropsPlantedFactory()


@pytest.fixture
def crops_planted_list(fake, harvest, farm):
    return [
        {
            "id": random.randint(1, 100000),
            "created_at": fake.iso8601(),
            "updated_at": fake.iso8601(),
            "harvest": harvest.id,
            "farm": farm.id,
            "product": "SOJA",
            "quantity": 100.00
        }
    ]


@pytest.fixture
def crops_planted_object(harvest, farm):
    return {
        "harvest": harvest.id,
        "farm": farm.id,
        "product": "soja",
        "quantity": 100.00
    }
