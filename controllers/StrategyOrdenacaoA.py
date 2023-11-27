from models import Jogo
from controllers import OrdenacaoStrategy


# Ordenação A: Quicksort
class StrategyOrdenacaoA(OrdenacaoStrategy):
    def ordenar(self, recuperarJogos):
        # Implementação do algoritmo de ordenação Quicksort
        return sorted(recuperarJogos, key=lambda jogo: jogo.avaliacao, reverse=True)
