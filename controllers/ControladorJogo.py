from models import FactoryJogo, BancoDeDados, SistemaJogosEletronicos

class ControladorJogo:
    def __init__(self, sistema):
        self.__banco_de_dados = BancoDeDados.BancoDeDados()
        self.__sistema = sistema

    @staticmethod
    def criarJogo(codigo, nome, descricao, desenvolvedora, dataLancamento, valor, requisitosMinimos, avaliacao, comentario, disponivel):
        jogo = FactoryJogo.factoryJogo(codigo, nome, descricao, desenvolvedora, dataLancamento, valor, requisitosMinimos, avaliacao, comentario, disponivel)
        return jogo


    def inserirJogo(self, jogo):
        if jogo != None:
            self.__banco_de_dados.inserirJogo(jogo)
            self.__sistema.atualizarDados()
        else:
            exception = ValueError("Invalid game: {}".format(jogo))
            raise exception


    def removerJogo(self, codigo):
        self.__banco_de_dados.removerJogo(codigo)
        self.__sistema.atualizarDados()


    def recuperarJogo(self, codigo):
        return self.__banco_de_dados.recuperarJogo(codigo)


    def recuperarJogos(self):
        return self.__banco_de_dados.recuperarJogos()