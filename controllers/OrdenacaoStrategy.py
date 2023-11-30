from abc import abstractmethod, ABC
qclass OrdenacaoStrategy(ABC):
    @abstractmethod
    def ordenar(self, recuperarJogos):
        pass