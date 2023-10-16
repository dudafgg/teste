def soma_numeros_pares(lista):
    soma = 0
    for numero in lista:
        if numero % 2 == 0: 
            soma += numero
    return soma
def main():
    lista = []  
    n = int(input("Quantos números deseja inserir na lista? "))
    
    for i in range(n):
        numero = int(input(f"Digite o {i+1}º número: "))
        lista.append(numero)
    
    resultado = soma_numeros_pares(lista)
    
    if resultado == 0:
        print("Resultado: A lista não contém números pares.")
    else:
        print(f"Resultado: A soma dos números pares é {resultado}.")

if __name__ == "__main__":
    main()
