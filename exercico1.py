def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def main():
    numero = int(input("Digite um número: "))
    if is_prime(numero):
        print(f"Resultado: O número {numero} é primo.")
    else:
        print(f"Resultado: O número {numero} não é primo.")

if __name__ == "__main__":
    main()
