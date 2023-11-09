class ItemVenda:
    def __init__(self, codigoProduto, valor, quantidade):
        self.__codigoProduto = codigoProduto
        self.__valor = valor
        self.__quantidade = quantidade

    def calcularTotal(self):
        return self.__valor * self.__quantidade

    #Getter's e Setter's

    @property
    def codigoProduto(self):
        return self.__codigoProduto

    @codigoProduto.setter
    def codigoProduto(self, codigoProduto):
        self.__codigoProduto = codigoProduto

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, valor):
        self.__valor = valor

    @property
    def quantidade(self):
        return self.__quantidade

    @quantidade.setter
    def quantidade(self, quantidade):
        self.__quantidade = quantidade
