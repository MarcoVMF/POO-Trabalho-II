class Venda:
    def __init__(self, codigo, cliente, gerente, dataVenda, dataEntrega, itensVenda, possuiItensFisico, valorTotal, valorComDesconto, formaPagamento, transportadora):
        self.__codigo = codigo
        self.__cliente = cliente
        self.__gerente = gerente
        self.__dataVenda = dataVenda
        self.__dataEntrega = dataEntrega
        self.__itensVenda = itensVenda
        self.__possuiItensFisico = possuiItensFisico
        self.__valorTotal = valorTotal
        self.__valorComDesconto = valorComDesconto
        self.__formaPagamento = formaPagamento
        self.__tranportadora = transportadora


    def calcularValorTotal(self):
        pass

    def calcularDataEntrega(self):
        pass

    def addItemVenda(self, itemVenda):
        pass

    #Getter's e Setter'
    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    @property
    def cliente(self):
        return self.__cliente

    @cliente.setter
    def cliente(self, cliente):
        self.__cliente = cliente

    @property
    def gerente(self):
        return self.__gerente

    @gerente.setter
    def gerente(self, gerente):
        self.__gerente = gerente

    @property
    def dataVenda(self):
        return self.__dataVenda

    @dataVenda.setter
    def dataVenda(self, dataVenda):
        self.__dataVenda = dataVenda

    @property
    def dataEntrega(self):
        return self.__dataEntrega

    @dataEntrega.setter
    def dataEntrega(self, dataEntrega):
        self.__dataEntrega = dataEntrega

    @property
    def itensVenda(self):
        return self.__itensVenda

    @itensVenda.setter
    def itensVenda(self, itensVenda):
        self.__itensVenda = itensVenda

    @property
    def possuiItensFisico(self):
        return self.__possuiItensFisico

    @possuiItensFisico.setter
    def possuiItensFisico(self, possuiItensFisico):
        self.__possuiItensFisico = possuiItensFisico

    @property
    def valorTotal(self):
        return self.__valorTotal

    @valorTotal.setter
    def valorTotal(self, valorTotal):
        self.__valorTotal = valorTotal

    @property
    def valorComDesconto(self):
        return self.__valorComDesconto

    @valorComDesconto.setter
    def valorComDesconto(self, valorComDesconto):
        self.__valorComDesconto = valorComDesconto

    @property
    def formaPagamento(self):
        return self.__formaPagamento

    @formaPagamento.setter
    def formaPagamento(self, formaPagamento):
        self.__formaPagamento = formaPagamento

    @property
    def transportadora(self):
        return self.__transportadora

    @transportadora.setter
    def transportadora(self, transportadora):
        self.__transportadora = transportadora

    #StringToString
    def __str__(self):
        return f"Código: {self.__codigo}\nCliente: {self.__cliente}\nGerente: {self.__gerente}\nData da Venda: {self.__dataVenda}\nData da Entrega: {self.__dataEntrega}\nItens da Venda: {self.__itensVenda}\nPossui Itens Físicos: {self.__possuiItensFisico}\nValor Total: {self.__valorTotal}\nValor com Desconto: {self.__valorComDesconto}\nForma de Pagamento: {self.__formaPagamento}\nTransportadora: {self.__transportadora}"
