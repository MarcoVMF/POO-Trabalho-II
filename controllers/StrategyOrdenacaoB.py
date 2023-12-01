from controllers.OrdenacaoStrategy import EstrategiaOrdenacao

# Estratégia B: Bubblesort
class EstrategiaBubblesort(EstrategiaOrdenacao):
    def ordenar(self, jogos):
        n = len(jogos)
        for i in range(n):
            for j in range(0, n-i-1):
                if jogos[j].avaliacao < jogos[j + 1].avaliacao:
                    jogos[j], jogos[j + 1] = jogos[j + 1], jogos[j]
        return jogos