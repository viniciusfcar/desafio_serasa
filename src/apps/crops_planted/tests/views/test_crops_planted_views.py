import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from utils import compare_dict_fields

@pytest.mark.django_db
def test_list_crops_planted(crops_planted, crops_planted_list):
    client = APIClient()

    url = reverse('crops_planted-list')
    response = client.get(url)
    response_data = response.json()

    assert response.status_code == status.HTTP_200_OK
    assert len(response_data) == len(crops_planted_list)
    compare_dict_fields(crops_planted_list[0], response_data[0])


@pytest.mark.django_db
def test_get_crops_planted(crops_planted):
    client = APIClient()

    args = crops_planted.id
    url = reverse('crops_planted-detail', args=[args])
    response = client.get(url)
    response_data = response.json()
    
    assert response.status_code == status.HTTP_200_OK
    assert response_data is not None
    assert response_data["farm"] == crops_planted.farm.id


@pytest.mark.django_db
def test_create_crops_planted(crops_planted_object):
    client = APIClient()
    
    url = reverse('crops_planted-list')
    response = client.post(url, data=crops_planted_object, format="json")
    response_data = response.json()

    assert response.status_code == status.HTTP_201_CREATED
    assert response_data is not None
    assert response_data["farm"] == crops_planted_object["farm"]
