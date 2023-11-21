from models import Transportadora, BancoDeDados, SistemaJogosEletronicos

class ControladorTransportadora:
    def __init__(self, sistema):
        self.__bancodedados = BancoDeDados.BancoDeDados()
        self.__sistema = sistema

    def criarTransportadora(self, codigo, cnpj, nome, email, telefone, endereco, tempoEntrega):
        transportadora = Transportadora.Transportadora(codigo, cnpj, nome, email, telefone, endereco, tempoEntrega)
        return transportadora

    def inserirTransportadora(self, transportadora):
        self.__bancodedados.inserirTransportadora(transportadora)
        self.__sistema.atualizarDados()

    def recuperarTransportadora(self, codigo):
        self.__bancodedados.recuperarTrasportadora(codigo)
        self.__sistema.atualizarDados()

    def removerTransportadora(self, codigo):
        self.__bancodedados.removerTransportadora(codigo)
        self.__sistema.atualizarDados()