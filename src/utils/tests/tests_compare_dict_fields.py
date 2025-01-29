import pytest
from utils.utils import compare_dict_fields

# Teste para o caso onde os dicionários têm as mesmas chaves
def test_compare_dict_fields_valid():
    dict1 = {"key1": "value1", "key2": "value2"}
    dict2 = {"key1": "value1", "key2": "value2"}

    compare_dict_fields(dict1, dict2)

# Teste para o caso onde as chaves dos dicionários são diferentes
def test_compare_dict_fields_keys_different():
    dict1 = {"key1": "value1", "key2": "value2"}
    dict2 = {"key3": "value3", "key4": "value4"}

    with pytest.raises(AssertionError, match="As chaves dos dicionários não são iguais"):
        compare_dict_fields(dict1, dict2)

# Teste para o caso onde um dos parâmetros não é um dicionário
def test_compare_dict_fields_invalid_type():
    dict1 = {"key1": "value1", "key2": "value2"}
    dict2 = ["value1", "value2"]

    with pytest.raises(ValueError, match="Ambos os parâmetros devem ser dicionários"):
        compare_dict_fields(dict1, dict2)
