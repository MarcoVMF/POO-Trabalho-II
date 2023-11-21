from models import Desenvolvedora, BancoDeDados, SistemaJogosEletronicos

class ControladorDesenvolvedora:
    def __init__(self):
        pass

    def criarDesenvolvedora(self, codigo, cnpj, nome, email, site, redeSocial, endereco):
        desenvolvedora = Desenvolvedora.Desenvolvedora(codigo, cnpj, nome, email, site, redeSocial, endereco)

    def inserirDesenvolvedora(self, desenvolvedora):
        BancoDeDados.BancoDeDados.inserirDesenvolvedora(desenvolvedora)
        SistemaJogosEletronicos.SistemaJogosEletronicos.atualizarDados()

    def recuperarDesenvolvedora(self, codigo):
        return BancoDeDados.BancoDeDados.recuperarDesenvolvedora(codigo)

    def removerDesenvolvedora(self, codigo):
        BancoDeDados.BancoDeDados.removerDesenvolvedora(codigo)
        SistemaJogosEletronicos.SistemaJogosEletronicos.atualizarDados()