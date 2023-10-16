import random
palavras = ["elefante", "banana", "computador", "python", "programacao", "jogador"]

def escolher_palavra():
    return random.choice(palavras)

def jogar_forca():
    palavra = escolher_palavra()
    letras_corretas = []
    tentativas_restantes = 6

    print("Bem-vindo ao Jogo da Forca!")
    
    while tentativas_restantes > 0:
        palavra_oculta = ""
        
        for letra in palavra:
            if letra in letras_corretas:
                palavra_oculta += letra
            else:
                palavra_oculta += "_"
        
        print("\nPalavra: " + palavra_oculta)
        print("Tentativas Restantes: " + str(tentativas_restantes))
        
        letra_escolhida = input("Escolha uma letra: ").lower()
        
        if len(letra_escolhida) != 1 or not letra_escolhida.isalpha():
            print("Por favor, escolha uma única letra válida.")
            continue
        
        if letra_escolhida in letras_corretas:
            print("Você já escolheu esta letra.")
            continue
        
        if letra_escolhida in palavra:
            print("Letra correta!")
            letras_corretas.append(letra_escolhida)
            
            if len(letras_corretas) == len(set(palavra)):
                print("\nResultado: Parabéns, você adivinhou a palavra!")
                break
        else:
            print("Letra incorreta. Tente novamente.")
            tentativas_restantes -= 1
    
    if tentativas_restantes == 0:
        print("\nResultado: Você esgotou suas tentativas. A palavra era '" + palavra + "'.")

jogar_forca()
