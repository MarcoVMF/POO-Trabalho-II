from abc import ABC, abstractmethod

# Estratégia: Interface para os algoritmos de ordenação
class EstrategiaOrdenacao(ABC):
    @abstractmethod
    def ordenar(self, lista_de_jogos):
        pass
