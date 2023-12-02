from models import Venda, ItemVenda, BancoDeDados, SistemaJogosEletronicos

class ControladorVendas:
    def __init__(self, sistema):
        self.__bancodedados = BancoDeDados.BancoDeDados()
        self.__sistema = sistema

    def criarVenda(self, codigo, cliente, gerente, dataVenda, dataEntrega, itensVenda, possuiItensFisico, valorTotal, valorComDesconto, formaPagamento, transportadora):
        venda = Venda.Venda(codigo, cliente, gerente, dataVenda, dataEntrega, itensVenda, possuiItensFisico, valorTotal, valorComDesconto, formaPagamento, transportadora)
        return venda

    def inserirVenda(self, venda):
        self.__bancodedados.inserirVenda(venda)
        self.__sistema.atualizarDados()

    def criarItemVenda(self, codigo, codigoProduto, valor, quantidade):
        itemVenda = ItemVenda.ItemVenda(codigo, codigoProduto, valor, quantidade)
        return itemVenda

    def recuperarPagamento(self, codigo, formaPagamento):
        return self.__bancodedados.recuperarFormaPagamento(codigo, formaPagamento)

    def inserirItemVenda(self, itemVenda):
        self.__bancodedados.inserirItemVenda(itemVenda)
        self.__sistema.atualizarDados()

    def recuperarItemVenda(self, codigo):
        return self.__bancodedados.recuperarItemVenda(codigo)

    def recuperarItensVenda(self):
        return self.__bancodedados.recuperarItensVenda()

    def removerItemVenda(self, codigo):
        self.__bancodedados.removerItemVenda(codigo)
        self.__sistema.atualizarDados()

    def recuperarVenda(self, codigo):
        return self.__bancodedados.recuperarVenda(codigo)

    def recuperarVendas(self):
        return self.__bancodedados.recuperarVendas()

    def removerVenda(self, codigo):
        self.__bancodedados.removerVenda(codigo)
        self.__sistema.atualizarDados()