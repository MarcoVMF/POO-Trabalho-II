from controllers.OrdenacaoStrategy import EstrategiaOrdenacao

# Estratégia A: Quicksort
class EstrategiaQuicksort(EstrategiaOrdenacao):
    def ordenar(self, recuperarJogos):
        # Implementação do algoritmo de ordenação Quicksort
        return sorted(recuperarJogos, key=lambda jogo: jogo.avaliacao, reverse=True)