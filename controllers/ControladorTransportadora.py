from models import Transportadora, BancoDeDados, SistemaJogosEletronicos

class ControladorTrabsportadora():
    def __init__(self):
        pass

    def criarTransportadora(self, codigo, cnpj, nome, email, telefone, endereco, tempoEntrega):
        transportadora = Transportadora.Transportadora(codigo, cnpj, nome, email, telefone, endereco, tempoEntrega)

    def inserirTransportadora(self, transportadora):
        BancoDeDados.BancoDeDados.inserirTransportadora(transportadora)
        SistemaJogosEletronicos.SistemaJogosEletronicos.atualizarDados()

    def recuperarTransportadora(self, codigo):
        BancoDeDados.BancoDeDados.recuperarTrasportadora(codigo)
        SistemaJogosEletronicos.SistemaJogosEletronicos.atualizarDados()

    def removerTransportadora(self, codigo):
        BancoDeDados.BancoDeDados.removerTransportadora(codigo)
        SistemaJogosEletronicos.SistemaJogosEletronicos.atualizarDados()