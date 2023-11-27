from controllers import ControladorJogo, ControladorVendas, ControladorDesenvolvedora
from models import Iterator, Pagamento

class ControladorRelatorios:
    def __init__(self, sistema):
        self.__controladorJogo = ControladorJogo.ControladorJogo(sistema)
        self.__controladorVenda = ControladorVendas.ControladorVendas(sistema)
        self.__controladorDesenvolvedora = ControladorDesenvolvedora.ControladorDesenvolvedora(sistema)

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


    # Terminar de implementar
    def listarVendasLucroDesenvolvedora(self, mes, desenvolvedora):
        vendas = self.__controladorVenda.recuperarVendas()
        produtos = self.__controladorJogo.recuperarJogos()

        lucro = 0
        conteudo = ''

        vendas = Iterator.Iterator(vendas)

        for venda in vendas:
            if venda.dataVenda.month == mes:
                itens = venda.itensVenda

                if isinstance(itens, list):
                    itens = Iterator.Iterator(itens)

                    for item in itens:
                        for produto in produtos:

                            if item.codigoProduto == produto.codigo:
                                if produto.desenvolvedora.nome == desenvolvedora:
                                    lucro = lucro + item.calcularTotal()
                                    conteudo.join(venda.__str__)
                                    conteudo.join('\n')
                else:
                    for produto in produtos:
                        if itens.codigoProduto == produto.codigo:
                            if produto.desenvolvedora.nome == desenvolvedora:
                                lucro = lucro + itens.calcularTotal()
                                conteudo.join(venda.__str__)
                                conteudo.join('\n')

        conteudo.join("Lucro total gerado:" + str(lucro))
        return conteudo

    def listarVendasPorBoleto(self):
        vendas = self.__controladorVenda.recuperarVendas()
        vendas = Iterator.Iterator(vendas)
        content = []
        for venda in vendas:
            pagamento = venda.formaPagamento
            if isinstance(pagamento, Pagamento.Boleto):
                content.append(venda)

        return content

    def listarVendasPorCartaoCredito(self):
        vendas = self.__controladorVenda.recuperarVendas()
        vendas = Iterator.Iterator(vendas)
        content = []
        for venda in vendas:
            pagamento = venda.formaPagamento
            if isinstance(pagamento, Pagamento.CartaoCredito):
                content.append(venda)

        return content

    def listarVendasPorPix(self):
        vendas = self.__controladorVenda.recuperarVendas()
        vendas = Iterator.Iterator(vendas)
        content = []
        for venda in vendas:
            pagamento = venda.formaPagamento
            if isinstance(pagamento, Pagamento.Pix):
                content.append(venda)

        return content

