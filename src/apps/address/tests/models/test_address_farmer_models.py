import pytest


@pytest.mark.django_db
def test_address_farmer_factory(address_farmer):
    assert address_farmer is not None
    assert address_farmer.city is not None