def e_palindromo(palavra):
    palavra = palavra.lower()  
    palavra = palavra.replace(" ", "")  
    return palavra == palavra[::-1]

def main():
    palavra = input("Digite uma palavra: ")
    if e_palindromo(palavra):
        print(f"Resultado: A palavra \"{palavra}\" é um palíndromo.")
    else:
        print(f"Resultado: A palavra \"{palavra}\" não é um palíndromo.")

if __name__ == "__main__":
    main()
