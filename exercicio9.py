def calcular_fatorial(n):
    if n == 0:
        return 1
    else:
        resultado = 1
        for i in range(1, n + 1):
            resultado *= i
        return resultado
    
numero = int(input("Calcular o fatorial de: "))
resultado = calcular_fatorial(numero)

print(f"Resultado: O fatorial de {numero} é {resultado}.")
