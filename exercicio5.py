def calcular_media(lista):
    if not lista:
        return None  
    soma = sum(lista)
    media = soma / len(lista)
    return media
def main():
    lista = []  
    while True:
        try:
            num = float(input("Digite um número (ou digite '0' para calcular a média): "))
            if num == 0:
                break
            lista.append(num)
        except ValueError:
            print("Entrada inválida. Por favor, digite um número válido.")

    media = calcular_media(lista)

    if media is None:
        print("A lista está vazia, não é possível calcular a média.")
    else:
        print(f"Resultado: A média dos números é {media}.")

if __name__ == "__main__":
    main()
