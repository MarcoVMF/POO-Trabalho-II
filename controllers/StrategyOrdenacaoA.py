#Ordenação A: Quicksort
class StrategyOrdenacaoA(StrategyOrdenacao):
    def ordenar(self, lista_de_jogos):
        # Implementação do algoritmo de ordenação Quicksort
        def quick_sort(arr):
            if len(arr) <= 1:
                return arr

            pivot = arr[len(arr) // 2]
            left = [x for x in arr if x < pivot]4
            right = [x for x in arr if x > pivot]

            return quick_sort(left) + [pivot] + quick_sort(right)
