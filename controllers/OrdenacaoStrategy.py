from abc import abstractmethod, ABC
class OrdenacaoStrategy(ABC):
    @abstractmethod
    def ordenar(self, recuperarJogos):
        pass