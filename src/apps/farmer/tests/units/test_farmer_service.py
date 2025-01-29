import pytest
from django.core.exceptions import ValidationError
from apps.farmer.services.farmer_service import validate_cpf_cnpj, definy_type_document

# Teste para validate_cpf_cnpj
@pytest.mark.parametrize(
    "document, should_raise, expected_error_message",
    [
        ("235.367.820-35", False, ""),  # CPF válido
        ("01653133074", False, ""),  # CPF válido (sem formatação)
        ("64.714.974/0001-10", False, ""),  # CNPJ válido
        ("77757311000124", False, ""),  # CNPJ válido (sem formatação)
        ("123.456.789-00", True, "O CPF fornecido é inválido."),  # CPF inválido
        ("12345678901234", True, "O CNPJ fornecido é inválido."),  # CNPJ inválido
        ("123456", True, "O valor deve ser um CPF ou CNPJ válido."),  # Tamanho inválido
    ],
)
def test_validate_cpf_cnpj(document, should_raise, expected_error_message):
    if should_raise:
        with pytest.raises(ValidationError) as excinfo:
            validate_cpf_cnpj(document)

        assert str(excinfo.value.message) == str(expected_error_message)
    else:
        try:
            validate_cpf_cnpj(document)
        except ValidationError as e:
            pytest.fail(f"validate_cpf_cnpj raised ValidationError unexpectedly: {e}")


# Teste para definy_type_document
@pytest.mark.parametrize(
    "document, expected_result",
    [
        ("235.367.820-35", "CPF"),  # CPF válido
        ("01653133074", "CPF"),  # CPF válido (sem formatação)
        ("64.714.974/0001-10", "CNPJ"),  # CNPJ válido
        ("77757311000124", "CNPJ"),  # CNPJ válido (sem formatação)
    ],
)
def test_definy_type_document(document, expected_result):
    result = definy_type_document(document)
    assert result == str(expected_result)
