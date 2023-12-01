from datetime import datetime, timedelta
class Venda:
    def __init__(self, codigo, cliente, gerente, dataVenda, dataEntrega, itensVenda, possuiItensFisico, valorTotal, valorComDesconto, formaPagamento, transportadora):
        self.__codigo = codigo
        self.__cliente = cliente
        self.__gerente = gerente
        self.__transportadora = transportadora
        self.__dataVenda = datetime.strptime(dataVenda, "%d/%m/%Y")
        self.__dataEntrega = self.calcularDataEntrega()
        self.__itensVenda = itensVenda
        self.__possuiItensFisico = possuiItensFisico
        self.__valorComDesconto = self.calcularValorTotal()
        self.__valorTotal = self.calcularValorTotal()
        self.__formaPagamento = formaPagamento


    def calcularValorTotal(self):
        aux = 0
        if isinstance(self.__itensVenda, list):
            for item in self.__itensVenda:
                aux += item.calcularTotal()
        else:
            aux += self.__itensVenda.calcularTotal()

        if self.__cliente.clienteEpico:
            aux = aux * 0.95

        return aux


    def calcularDataEntrega(self):
        return self.__dataVenda + timedelta(days=self.__transportadora.tempoEntrega)


    def addItemVenda(self, itemVenda):
        self.__itensVenda.append(itemVenda)

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

    def __str__(self):
        itens_str = ""
        if isinstance(self.__itensVenda, list):
            itens_str = "\n".join([str(item) for item in self.__itensVenda])
        else:
            itens_str = str(self.__itensVenda)

        return f"Código: {self.__codigo}\nCliente: {self.__cliente}\nGerente: {self.__gerente}\nData da Venda: {self.__dataVenda}\nData da Entrega: {self.__dataEntrega}\nItens da Venda:\n{itens_str}\nPossui Itens Físicos: {self.__possuiItensFisico}\nValor Total: {self.__valorTotal}\nValor com Desconto: {self.__valorComDesconto}\nForma de Pagamento: {self.__formaPagamento}\nTransportadora: {self.__transportadora}"
