from controllers import OrdenacaoStrategy
class Contexto:
    def __init__(self, estrategia):
        self._estrategia = estrategia

    def executar(self, recuperarJogos):
        return self._estrategia.ordenar(recuperarJogos)