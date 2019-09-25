
class Conta:

    def __init__(self, numero, titular, saldo, limite):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def extrato(self):
        print("Número conta: {} \nTitular: {} \nSaldo: {} \nLimite disponível: {}".format(self.numero, self.titular, self.saldo, self.limite))


    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        self.saldo -= valor


