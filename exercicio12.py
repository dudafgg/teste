class Banco:
    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial

    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
            return True
        else:
            return False

    def saque(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            return True
        else:
            return False

    def verificar_saldo(self):
        return self.saldo

banco_cenario1 = Banco(500)
deposito = 200
saque = 100

if banco_cenario1.deposito(deposito) and banco_cenario1.saque(saque):
    print("Resultado: Saldo atual: R$", banco_cenario1.verificar_saldo())
else:
    print("Resultado: Operações de depósito e saque não puderam ser concluídas.")

banco_cenario2 = Banco(100)
saque_cenario2 = 200

if banco_cenario2.saque(saque_cenario2):
    print("Resultado: Saldo atual: R$", banco_cenario2.verificar_saldo())
else:
    print("Resultado: Saldo insuficiente para realizar o saque.")
