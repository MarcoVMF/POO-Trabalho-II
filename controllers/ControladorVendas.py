from models import Venda, BancoDeDados, SistemaJogosEletronicos

class ControladorVendas:
    def __init__(self):
        pass

    def criarVenda(self, codigo, cliente, gerente, dataVenda, dataEntrega, itensVenda, possuiItensFisico, valorTotal, valorComDesconto, formaPagamento, transportadora):
        venda = Venda.Venda(codigo, cliente, gerente, dataVenda, dataEntrega, itensVenda, possuiItensFisico, valorTotal, valorComDesconto, formaPagamento, transportadora)

    def inserirVenda(self, venda):
        BancoDeDados.BancoDeDados.inserirVenda(venda)
        SistemaJogosEletronicos.SistemaJogosEletronicos.atualizarDados()

    def recuperarVenda(self, codigo):
        return BancoDeDados.BancoDeDados.recuperarVenda(codigo)

    def removerVenda(self, codigo):
        BancoDeDados.BancoDeDados.removerVenda(codigo)
        SistemaJogosEletronicos.SistemaJogosEletronicos.atualizarDados()