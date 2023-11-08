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

    

    #Getter's e Setter'