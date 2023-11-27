from models import Desenvolvedora, BancoDeDados, SistemaJogosEletronicos

class ControladorDesenvolvedora:
    def __init__(self, sistema):
        self.__bancodedados = BancoDeDados.BancoDeDados()
        self.__sistema = sistema

    def criarDesenvolvedora(self, codigo, cnpj, nome, email, site, redeSocial, endereco):
        desenvolvedora = Desenvolvedora.Desenvolvedora(codigo, cnpj, nome, email, site, redeSocial, endereco)
        return desenvolvedora

    def inserirDesenvolvedora(self, desenvolvedora):
        self.__bancodedados.inserirDesenvolvedora(desenvolvedora)
        self.__sistema.atualizarDados()

    def recuperarDesenvolvedora(self, codigo):
        return self.__bancodedados.recuperarDesenvolvedora(codigo)

    def recuperarDesenvolvedoras(self):
        return self.__bancodedados.recuperarDesenvolvedoras()

    def removerDesenvolvedora(self, codigo):
        self.__bancodedados.removerDesenvolvedora(codigo)
        self.__sistema.atualizarDados()