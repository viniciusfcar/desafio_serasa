import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from utils import compare_dict_fields

@pytest.mark.django_db
def test_list_harvest(harvest, harvest_list):
    client = APIClient()

    url = reverse('harvest-list')
    response = client.get(url)
    response_data = response.json()

    assert response.status_code == status.HTTP_200_OK
    assert len(response_data) == len(harvest_list)
    compare_dict_fields(harvest_list[0], response_data[0])


@pytest.mark.django_db
def test_get_harvest(harvest):
    client = APIClient()

    args = harvest.id
    url = reverse('harvest-detail', args=[args])
    response = client.get(url)
    response_data = response.json()
    
    assert response.status_code == status.HTTP_200_OK
    assert response_data is not None
    assert response_data["name"] == harvest.name
    assert response_data["year"] == harvest.year


@pytest.mark.django_db
def test_create_harvest(harvest_object):
    client = APIClient()
    
    url = reverse('harvest-list')
    response = client.post(url, data=harvest_object, format="json")
    response_data = response.json()

    assert response.status_code == status.HTTP_201_CREATED
    assert response_data is not None
    assert response_data["name"] == harvest_object["name"]
    assert response_data["year"] == harvest_object["year"]
