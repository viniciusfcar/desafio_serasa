import pytest


@pytest.mark.django_db
def test_address_farm_factory(address_farm):
    assert address_farm is not None
    assert address_farm.city is not None