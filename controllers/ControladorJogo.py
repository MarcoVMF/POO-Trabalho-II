from models import FactoryJogo, BancoDeDados, SistemaJogosEletronicos

class ControladorJogo:
    def __init__(self):
        pass

    def criarJogo(self, codigo, nome, descricao, desenvolvedora, dataLancamento, valor, requisitosMinimos, avaliacao, comentario, disponivel):
        jogo = FactoryJogo.factoryJogo(codigo, nome, descricao, desenvolvedora, dataLancamento, valor, requisitosMinimos, avaliacao, comentario, disponivel)
        return jogo

    def inserirJogo(self, jogo):
        if jogo != None:
            BancoDeDados.BancoDeDados.inserirJogo(jogo)
            SistemaJogosEletronicos.SistemaJogosEletronicos.atualizarDados()
        else:
            exception = ValueError("Invalid game: {}".format(jogo))
            raise exception

    def removerJogo(self, codigo):
        BancoDeDados.BancoDeDados.removerJogo(codigo)
        SistemaJogosEletronicos.SistemaJogosEletronicos.atualizarDados()

    def recuperarJogo(self, codigo):
        return BancoDeDados.BancoDeDados.recuperarJogo(codigo)

    def recuperarJogos(self):
        return BancoDeDados.BancoDeDados.recuperarJogos()