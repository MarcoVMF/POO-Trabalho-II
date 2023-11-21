from controllers import ControladorJogo

class ControladorRelatorios:
    def __init__(self):
        self.__controladorJogo = ControladorJogo.ControladorJogo()

    #
    def listarJogos(self, tipoJogo):
        conteudo = []
        jogos = self.__controladorJogo.recuperarJogos()
        for jogo in jogos:
            if isinstance(jogo, tipoJogo):
                conteudo.append(jogo)

        return conteudo

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

    def listarJogosMaisCaros(self):
        content = []
        arr = self.ordenacao()
        for i in range(0, 10):
            content.push(arr[i])

        return content

    def listasJogosMaisBaratos(self):
        content = []
        arr = self.ordenacao()
        for i in range(len(arr)-10, len(arr)):
            content.push(arr[i])

        return content

