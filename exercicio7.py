def busca_binaria(lista, elemento):
    inicio = 0
    fim = len(lista) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2

        if lista[meio] == elemento:
            return meio
        elif lista[meio] < elemento:
            inicio = meio + 1
        else:
            fim = meio - 1

    return -1

lista1 = [1, 3, 5, 7, 9, 11, 13, 15]
elemento1 = 7
resultado1 = busca_binaria(lista1, elemento1)

if resultado1 != -1:
    print(f"Resultado: O número {elemento1} foi encontrado na posição {resultado1}.")
else:
    print(f"Resultado: O número {elemento1} não foi encontrado na lista.")

lista2 = [2, 4, 6, 8, 10]
elemento2 = 3
resultado2 = busca_binaria(lista2, elemento2)

if resultado2 != -1:
    print(f"Resultado: O número {elemento2} foi encontrado na posição {resultado2}.")
else:
    print(f"Resultado: O número {elemento2} não foi encontrado na lista.")
