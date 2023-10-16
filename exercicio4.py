frase = input("Digite uma frase: ")
palavras = frase.strip().split()

if not palavras:
    print("Resultado: A frase não possui palavras.")
else:
    numero_de_palavras = len(palavras)
    print(f"Resultado: A frase possui {numero_de_palavras} palavras.")
