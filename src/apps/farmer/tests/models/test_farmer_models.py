import pytest


@pytest.mark.django_db
def test_farmer_factory(farmer):
    assert farmer is not None
    assert farmer.name is not None