import pytest


@pytest.mark.django_db
def test_crops_planted_factory(crops_planted):
    assert crops_planted is not None
    assert crops_planted.farm is not None
    assert crops_planted.harvest is not None