from models import Venda, BancoDeDados, SistemaJogosEletronicos

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

    def recuperarVenda(self, codigo):
        return self.__bancodedados.recuperarVenda(codigo)

    def removerVenda(self, codigo):
        self.__bancodedados.removerVenda(codigo)
        self.__sistema.atualizarDados()