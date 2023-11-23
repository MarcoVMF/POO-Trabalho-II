#Ordenação B: Bubblesort
class: StrategyOrdenacaoB(StrategyOrdenacao):
    def ordenar(self, lista_de_jogos):
        # Implementação do algoritmo de ordenação Bubblesort
        n = len(lista_de_jogos)
        for i in range(n):
            for j in range(0, n-i-1):
                if lista_de_jogos[j].avaliacao < lista_de_jogos[j+1].avaliacao:
                    lista_de_jogos[j], lista_de_jogos[j+1] = lista_de_jogos[j+1], lista_de_jogos[j]
        return lista_de_jogo