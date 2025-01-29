import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from utils import compare_dict_fields

@pytest.mark.django_db
def test_list_address_farmer(address_farmer, address_farmer_list):
    client = APIClient()

    url = reverse('address_farmer-list')
    response = client.get(url)
    response_data = response.json()

    assert response.status_code == status.HTTP_200_OK
    assert len(response_data) == len(address_farmer_list)
    compare_dict_fields(address_farmer_list[0], response_data[0])


@pytest.mark.django_db
def test_get_address_farmer(address_farmer):
    client = APIClient()

    args = address_farmer.id
    url = reverse('address_farmer-detail', args=[args])
    response = client.get(url)
    response_data = response.json()
    
    assert response.status_code == status.HTTP_200_OK
    assert response_data is not None
    assert response_data["postal_code"] == address_farmer.postal_code


@pytest.mark.django_db
def test_create_address_farmer(address_farmer_object):
    client = APIClient()
    
    url = reverse('address_farmer-list')
    response = client.post(url, data=address_farmer_object, format="json")
    response_data = response.json()

    assert response.status_code == status.HTTP_201_CREATED
    assert response_data is not None
    assert response_data["postal_code"] == address_farmer_object["postal_code"]
