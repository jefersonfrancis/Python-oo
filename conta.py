
class Conta:

    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Número conta: {} \nTitular: {} \nSaldo: {} \nLimite disponível: {}".format(self.__numero, self.__titular, self.__saldo, self.__limite))


    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor


