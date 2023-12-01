import random, string
from abc import ABC, abstractmethod

class Pagamento(ABC):
    def __init__(self, codigo):
        self.__codigo = codigo

    def __str__(self):
        return (f"Codigo: {self.codigo}")

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
        return (f"\n======Boleto======"
                f"\nCodigo: {super().codigo}"
                f"\nNumero: {self.numero}"
                f"\n==================\n")

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
        return (f"\n======Cartao Credito======"
                f"\nCodigo: {super().codigo}"
                f"\nNome: {self.nome}"
                f"\nBandeira: {self.bandeira}"
                f"\nNumero: {self.numero}"
                f"\n==================\n")

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
        return (f"\n======Pix======"
                f"\nCodigo: {super().codigo}"
                f"\nCodigo Pix: {self.codigoPix}"
                f"\n==================\n")

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
