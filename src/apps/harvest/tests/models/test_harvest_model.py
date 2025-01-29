import pytest


@pytest.mark.django_db
def test_harvest_factory(harvest):
    assert harvest is not None
    assert harvest.name is not None
    assert harvest.year is not None