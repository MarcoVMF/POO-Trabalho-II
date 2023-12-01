from controllers.OrdenacaoStrategy import EstrategiaOrdenacao

# Estratégia B: Bubblesort
class EstrategiaBubblesort(EstrategiaOrdenacao):
    def ordenar(self, recuperarJogos):
        # Implementação do algoritmo de ordenação Bubblesort
        n = len(recuperarJogos)
        for i in range(n):
            for j in range(0, n-i-1):
                if recuperarJogos[j].avaliacao < recuperarJogos[j+1].avaliacao:
                    recuperarJogos[j], recuperarJogos[j+1] = recuperarJogos[j+1], recuperarJogos[j]
        return recuperarJogos