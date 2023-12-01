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
    def listarJogosMaisBaratos(self):
        content = []
        arr = self.ordenacao()
        for i in range(0, 10):
            content.append(arr[i])

        return content


    #Listar jogos ordenados de forma crescente por nota de avaliação (Strategy)
    def listarStrategy(self):
        jogos = self.__controladorJogo.recuperarJogos()
        return jogos


    def listarTodasDesenvolvedoras(self):
        desenvolvedoras = self.__controladorDesenvolvedora.recuperarDesenvolvedoras()
        return desenvolvedoras

    #Listar as 10 desenvolvedoras com mais jogos vendidos
    def listarDesenvolvedorasMaisJogosVendidos(self):
            desenvolvedoras_vendas = {}
            jogos = self.__controladorJogo.recuperarJogos()

            for jogo in jogos:
                desenvolvedora = jogo.desenvolvedora
                vendas = self.__controladorJogo.recuperarVendas(jogo)

                if desenvolvedora not in desenvolvedoras_vendas:
                    desenvolvedoras_vendas[desenvolvedora] = 0

                desenvolvedoras_vendas[
                    desenvolvedora] += 1  # Conta o número de jogos vendidos

            # Ordena as desenvolvedoras por número de jogos vendidos em ordem decrescente
            desenvolvedoras_sorted = sorted(desenvolvedoras_vendas.items(), key=lambda x: x[1], reverse=True)

            return desenvolvedoras_sorted

   #Listar as 10 desenvolvedoras com maior lucro
    def listarDesenvolvedorasMaiorLucro(self):
        desenvolvedoras_lucro = {}
        jogos = self.__controladorJogo.recuperarJogos()

        for jogo in jogos:
            desenvolvedora = jogo.desenvolvedora
            lucro = self.__controladorJogo.recuperarLucro(jogo)

            if desenvolvedora not in desenvolvedoras_lucro:
                desenvolvedoras_lucro[desenvolvedora] = 0

            desenvolvedoras_lucro[desenvolvedora] += lucro

        # Ordena as desenvolvedoras por lucro em ordem decrescente
        desenvolvedoras_sorted = sorted(desenvolvedoras_lucro.items(), key=lambda x: x[1], reverse=True)[:10]

        # Exibe o lucro bruto geral
        lucro_geral = controladorVendas.RecuperarVendas()
        print(f"Lucro Bruto Geral: {lucro_geral}")
        controladorVendas = ControladorVendas()  # Substitua com a criação real do ControladorVendas
        resultado = controladorRelatorios.listarDesenvolvedorasMaiorLucro(controladorVendas)

        return desenvolvedoras_sorted






    #Terminar de implementar
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

