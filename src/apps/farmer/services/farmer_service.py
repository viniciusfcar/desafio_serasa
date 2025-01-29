from django.core.exceptions import ValidationError
from validate_docbr import CPF, CNPJ


def validate_cpf_cnpj(valor):
    valor = valor.translate(str.maketrans("", "", "./-"))
    cpf = CPF()
    cnpj = CNPJ()

    if len(valor) == 11:
        if not cpf.validate(valor):
            raise ValidationError("O CPF fornecido é inválido.")
        
    elif len(valor) == 14:
        if not cnpj.validate(valor):
            raise ValidationError("O CNPJ fornecido é inválido.")
        
    else:
        raise ValidationError("O valor deve ser um CPF ou CNPJ válido.")


def definy_type_document(valor):
    valor = valor.translate(str.maketrans("", "", "./-"))
    cpf = CPF()

    if cpf.validate(valor):
        return "CPF"
    
    else:
        return "CNPJ"