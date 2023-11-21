import models.Jogo as Jogo

class factoryJogo:

    @staticmethod
    def factory(tipo, codigo, nome, descricao, desenvolvedora, dataLancamento, valor, requisitosMinimos, avaliacao, comentario, disponivel):
        if tipo == 'Acao':
            return Jogo.Acao(codigo, nome, descricao, desenvolvedora, dataLancamento, valor, requisitosMinimos, avaliacao, comentario, disponivel, tipo)
        elif tipo == 'Aventura':
            return Jogo.Aventura(codigo, nome, descricao, desenvolvedora, dataLancamento, valor, requisitosMinimos, avaliacao, comentario, disponivel, tipo)
        elif tipo == 'RPG':
            return Jogo.RPG(codigo, nome, descricao, desenvolvedora, dataLancamento, valor, requisitosMinimos, avaliacao, comentario, disponivel, tipo)
        elif tipo == 'Esporte':
            return Jogo.Esporte(codigo, nome, descricao, desenvolvedora, dataLancamento, valor, requisitosMinimos, avaliacao, comentario, disponivel, tipo)
        elif tipo == 'Corrida':
            return Jogo.Corrida(codigo, nome, descricao, desenvolvedora, dataLancamento, valor, requisitosMinimos, avaliacao, comentario, disponivel, tipo)
        else:
            raise ValueError("Invalid game type: {}".format(tipo))
