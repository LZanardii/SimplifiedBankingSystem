from validate_docbr import CPF

def validateCpf(cpf_inserido):
    cpf = CPF()
    return cpf.validate(cpf_inserido)