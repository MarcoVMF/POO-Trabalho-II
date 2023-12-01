class ItemVenda:
    def __init__(self, codigo, codigoProduto, valor, quantidade):
        self.__codigo = codigo
        self.__codigoProduto = codigoProduto
        self.__valor = valor
        self.__quantidade = quantidade

    def calcularTotal(self):
        return self.__valor * self.__quantidade

    #Getter's e Setter's

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo


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

    #StringToString
    def __str__(self):
        return f'Código: {self.__codigo} - Código Produto: {self.__codigoProduto} - Valor: {self.__valor} - Quantidade: {self.__quantidade}'
