import random, string
from abc import ABC, abstractmethod

class Pagamento(ABC):
    def __init__(self, codigo):
        self.__codigo = codigo

    def __str__(self):
        return f"Codigo da Nota: {self.codigo}"

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigoNota):
        self.__codigo = codigoNota

class Boleto(Pagamento):
    def __init__(self, codigo, numero):
        super().__init__(codigo)
        self.__numero = numero

    def __str__(self):
        pagamentoStr = super().__str__()
        return f"{pagamentoStr}\n" \
               f"Numero: {self.__numero}"

    @property
    def numero(self):
        return self.__numero

    @numero.setter
    def numero(self, numero):
        self.__numero = numero

class CartaoCredito(Pagamento):

    def __init__(self, codigo, nome, bandeira, numero):
        super().__init__(codigo)
        self.__nome = nome
        self.__bandeira = bandeira
        self.__numero = numero

    def __str__(self):
        pagamentoStr = super().__str__()
        return f"{pagamentoStr}\n" \
               f"Nome: {self.__nome}\n" \
               f"Bandeira: {self.__bandeira}\n" \
               f"Numero: {self.__numero}"

    @property
    def nome(self):
        return self.__nome

    @property
    def bandeira(self):
        return self.__bandeira

    @property
    def numero(self):
        return self.__numero

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @bandeira.setter
    def bandeira(self, bandeira):
        self.__bandeira = bandeira

    @numero.setter
    def numero(self, numero):
        self.__numero = numero

class Pix(Pagamento):
    def __init__(self, codigo, codigoPix):
        super().__init__(codigo)
        self.__codigoPix = codigoPix

    def __str__(self):
        pagamentoStr = super().__str__()
        return f"{pagamentoStr}\n" \
               f"Codigo Pix: {self.__codigoPix}"

    def gerarCodigoPix(self):
        size = 30
        chars = string.ascii_uppercase + string.digits
        return ''.join(random.choice(chars) for _ in range(size))


    @property
    def codigoPix(self):
        return self.__codigoPix

    @codigoPix.setter
    def codigoPix(self, codigoPix):
        self.__codigoPix = codigoPix
