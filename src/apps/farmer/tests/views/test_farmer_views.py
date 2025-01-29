import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from utils import compare_dict_fields

@pytest.mark.django_db
def test_list_farmer(farmer, farmer_list):
    client = APIClient()

    url = reverse('farmer-list')
    response = client.get(url)
    response_data = response.json()

    assert response.status_code == status.HTTP_200_OK
    assert len(response_data) == len(farmer_list)
    compare_dict_fields(farmer_list[0], response_data[0])


@pytest.mark.django_db
def test_get_farmer(farmer):
    client = APIClient()

    args = farmer.id
    url = reverse('farmer-detail', args=[args])
    response = client.get(url)
    response_data = response.json()
    
    assert response.status_code == status.HTTP_200_OK
    assert response_data is not None
    assert response_data["name"] == farmer.name


@pytest.mark.django_db
def test_create_farmer(farmer_object):
    client = APIClient()
    
    url = reverse('farmer-list')
    response = client.post(url, data=farmer_object, format="json")
    response_data = response.json()

    assert response.status_code == status.HTTP_201_CREATED
    assert response_data is not None
    assert response_data["name"] == farmer_object["name"]
