
class Conta:

    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular.title()
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Número conta: {} \nTitular: {} \nSaldo: {} \nLimite disponível: {}".format(self.__numero, self.__titular, self.__saldo, self.__limite))


    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor


    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)
        print("Transação efetuada com sucesso!")

    @property
    def saldo(self):
        return self.__saldo


    def get_titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite
