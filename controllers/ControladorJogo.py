from models import FactoryJogo, BancoDeDados, SistemaJogosEletronicos

class ControladorJogo:
    def __init__(self):
        self.__bancodedados = BancoDeDados.BancoDeDados()

    @staticmethod
    def criarJogo(codigo, nome, descricao, desenvolvedora, dataLancamento, valor, requisitosMinimos, avaliacao, comentario, disponivel):
        jogo = FactoryJogo.factoryJogo(codigo, nome, descricao, desenvolvedora, dataLancamento, valor, requisitosMinimos, avaliacao, comentario, disponivel)
        return jogo


    def inserirJogo(self, jogo):
        if jogo != None:
            self.__bancodedados.inserirJogo(jogo)
            SistemaJogosEletronicos.SistemaJogosEletronicos.atualizarDados()
        else:
            exception = ValueError("Invalid game: {}".format(jogo))
            raise exception


    def removerJogo(self, codigo):
        self.__bancodedados.removerJogo(codigo)
        SistemaJogosEletronicos.SistemaJogosEletronicos.atualizarDados()


    def recuperarJogo(self, codigo):
        return self.__bancodedados.recuperarJogo(codigo)


    def recuperarJogos(self):
        return self.__bancodedados.recuperarJogos()