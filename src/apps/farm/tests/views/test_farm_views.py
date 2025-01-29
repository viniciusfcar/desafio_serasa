import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from utils import compare_dict_fields

@pytest.mark.django_db
def test_list_farm(farm, farm_list):
    client = APIClient()

    url = reverse('farm-list')
    response = client.get(url)
    response_data = response.json()

    assert response.status_code == status.HTTP_200_OK
    assert len(response_data) == len(farm_list)
    compare_dict_fields(farm_list[0], response_data[0])


@pytest.mark.django_db
def test_get_farm(farm):
    client = APIClient()

    args = farm.id
    url = reverse('farm-detail', args=[args])
    response = client.get(url)
    response_data = response.json()
    
    assert response.status_code == status.HTTP_200_OK
    assert response_data is not None


@pytest.mark.django_db
def test_create_farm(farm_object):
    client = APIClient()
    
    url = reverse('farm-list')
    response = client.post(url, data=farm_object, format="json")
    response_data = response.json()

    assert response.status_code == status.HTTP_201_CREATED
    assert response_data is not None


@pytest.mark.django_db
def test_quantity_all_farms(farm):
    client = APIClient()
    
    url = "/api/farm/quantity_all_farms/"

    response = client.get(url)
    
    assert response.status_code == status.HTTP_200_OK
    assert response.data == 1


@pytest.mark.django_db
def test_quantity_all_total_area_farms(farm):
    client = APIClient()
    
    url = "/api/farm/quantity_all_total_area_farms/"

    response = client.get(url)
    
    assert response.status_code == status.HTTP_200_OK
    assert response.data == farm.total_area_farm
