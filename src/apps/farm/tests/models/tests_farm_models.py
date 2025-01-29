import pytest


@pytest.mark.django_db
def test_farm_factory(farm):
    assert farm is not None
    assert farm.farmer is not None