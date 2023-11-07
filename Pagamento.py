from abc import ABC, abstractmethod

class Pagamento(ABC):
    def __init__(self, codigoNota):
        self.__codigoNota = codigoNota

    def __str__(self):
        return f"Codigo da Nota: {self.__codigoNota}"

    @property
    def codigoNota(self):
        return self.__codigoNota

    @codigoNota.setter
    def codigoNota(self, codigoNota):
        self.__codigoNota = codigoNota

class Boleto(Pagamento):
    def __init__(self, codigoNota, numero):
        super().__init__(codigoNota)
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

    def __init__(self, codigoNota, nome, bandeira, numero):
        super().__init__(codigoNota)
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
    def __init__(self, codigoNota, codigoPix):
        super().__init__(codigoNota)
        self.__codigoPix = codigoPix

    def __str__(self):
        pagamentoStr = super().__str__()
        return f"{pagamentoStr}\n" \
               f"Codigo Pix: {self.__codigoPix}"

    @property
    def codigoPix(self):
        return self.__codigoPix

    @codigoPix.setter
    def codigoPix(self, codigoPix):
        self.__codigoPix = codigoPix

