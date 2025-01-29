import pytest
from faker import Faker
import random
from farm.factories import FarmFactory
from apps.address.tests.conftest import address_farm
from apps.farmer.tests.conftest import farmer


@pytest.fixture
def fake():
    return Faker("pt_BR")


@pytest.fixture
def farm():
    return FarmFactory()


@pytest.fixture
def farm_list(fake, address_farm, farmer):
    return [
        {
            "id": random.randint(1, 100000),
            "created_at": fake.iso8601(),
            "updated_at": fake.iso8601(),
            "farmer": farmer.id,
            "name_farm": fake.user_name(),
            "address": address_farm.id,
            "total_area_farm": 100.00,
            "agricultural_area": 70.00,
            "vegetation_area": 30.00
        }
    ]


@pytest.fixture
def farm_object(fake, address_farm, farmer):
    return {
        "name_farm": fake.user_name(),
        "farmer": farmer.id,
        "address": address_farm.id,
        "total_area_farm": 100.00,
        "agricultural_area": 70.00,
        "vegetation_area": 30.00
    }
