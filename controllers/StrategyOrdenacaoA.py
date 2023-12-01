from controllers.OrdenacaoStrategy import EstrategiaOrdenacao

# Estratégia A: SelectionSort
class EstrategiaSelectionSort(EstrategiaOrdenacao):
    def ordenar(self, jogos):
        for i in range(len(jogos)):
            max_index = i
            for j in range(i + 1, len(jogos)):
                aux1 = jogos[max_index].avaliacao
                aux2 = jogos[j].avaliacao
                if aux1 < aux2:
                    max_index = j
            jogos[i], jogos[max_index] = jogos[max_index], jogos[i]

        return jogos
