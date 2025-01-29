import pytest
from django.core.exceptions import ValidationError
from apps.farm.services.farm_service import validation_total_area

# Teste para o caso válido
def test_validation_total_area_valid():
    total_area = 100
    agricultural_area = 30
    vegetation_area = 40

    try:
        validation_total_area(total_area, agricultural_area, vegetation_area)
    except ValidationError:
        pytest.fail("ValidationError foi levantada inesperadamente")

# Teste para o caso inválido
def test_validation_total_area_invalid():
    total_area = 100
    agricultural_area = 60
    vegetation_area = 50

    with pytest.raises(ValidationError, match="As áreas de agricultura e vegetação somadas, ultrapassam a área total."):
        validation_total_area(total_area, agricultural_area, vegetation_area)
