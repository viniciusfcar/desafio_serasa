from datetime import datetime

# Função para comparar os campos de dois dicionários
def compare_dict_fields(dict1, dict2):
    
    if not isinstance(dict1, dict) or not isinstance(dict2, dict):
        raise ValueError("Ambos os parâmetros devem ser dicionários.")
    
    # Compara as chaves dos dicionários
    keys1 = set(dict1.keys())
    keys2 = set(dict2.keys())
    
    # Verifica se as chaves são iguais
    if keys1 != keys2:
        raise AssertionError(f"As chaves dos dicionários não são iguais. Dict1: {keys1}, Dict2: {keys2}")
