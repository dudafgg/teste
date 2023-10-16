import re

def validar_senha(senha):
    if len(senha) < 8:
        return False

    if not re.search(r'[A-Z]', senha):
        return False

    if not re.search(r'[a-z]', senha):
        return False

    
    if not re.search(r'\d', senha):
        return False

    return True

senha = input("Digite a senha: ")

if validar_senha(senha):
    print("Resultado: A senha é válida.")
else:
    print("Resultado: A senha é inválida. A senha deve atender aos critérios especificados.")
