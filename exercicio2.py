def contar_vogais(frase):
    vogais = "AEIOUaeiou"
    contador = 0
    
    for letra in frase:
        if letra in vogais:
            contador += 1
    
    return contador

def main():
    frase = input("Digite uma frase: ")
    
    num_vogais = contar_vogais(frase)
    
    if num_vogais > 0:
        print(f"Resultado: A frase possui {num_vogais} vogais.")
    else:
        print("Resultado: A frase não possui vogais.")

if __name__ == "__main__":
    main()
