from validate_docbr import CPF

def validate_cpf(cpf_inserido):
    cpf = CPF()
    return cpf.validate(cpf_inserido)

def tratar_dado_unico(dado):
    dado = dado.replace('\'', '')
    dado = dado.replace('(', '')
    dado = dado.replace(')', '')
    dado = dado.replace(',', '')
    return dado