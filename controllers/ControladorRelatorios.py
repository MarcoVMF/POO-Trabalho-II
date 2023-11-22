from controllers import ControladorJogo
from models import Iterator

class ControladorRelatorios:
    def __init__(self, sistema):
        self.__controladorJogo = ControladorJogo.ControladorJogo(sistema)

    #Listar todos os jogos e todos os jogos de um tipo específico
    def listarJogos(self, tipoJogo):
        conteudo = []
        jogos = self.__controladorJogo.recuperarJogos()
        jogos = Iterator.Iterator(jogos)
        for jogo in jogos:
            if isinstance(jogo, tipoJogo):
                conteudo.append(jogo)

        return conteudo

    #Ordenação usada para listar os jogos mais caros e mais baratos
    def ordenacao(self):
        jogos = self.__controladorJogo.recuperarJogos()
        arr = jogos
        for i in range(len(jogos)):
            min = i
            for j in range(i + 1, len(jogos)):
                aux1 = arr[min].valor
                aux2 = arr[j].valor
                if aux1 > aux2:
                    min = j
            arr[i], arr[min] = arr[min], arr[i]

        return arr

    #Listar os 10 jogos mais caros
    def listarJogosMaisCaros(self):
        content = []
        arr = self.ordenacao()
        for i in range(len(arr)-1, len(arr)-11, -1):
            content.append(arr[i])

        return content

    #Listar os 10 jogos mais baratos
    def listasJogosMaisBaratos(self):
        content = []
        arr = self.ordenacao()
        for i in range(0, 10):
            content.append(arr[i])

        return content

