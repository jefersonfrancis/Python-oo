
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

    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_a_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_a_sacar

    def sacar(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("Valor ultrapassa o saldo disponível, entrar em contato com seu gerente.")


    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)
        print("Transação efetuada com sucesso!")

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigo_do_banco():
        return "001"


    @staticmethod
    def codigos_dos_bancos():
        return {"BB" : "001", "Caixa" : "104", "Bradesco" : "237"}