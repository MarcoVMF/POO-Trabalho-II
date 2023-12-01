from controllers import ControladorJogo, ControladorVendas, ControladorDesenvolvedora, ControladorTransportadora, ControladorUsuario
from models import Iterator, Pagamento

class ControladorRelatorios:
    def __init__(self, sistema):
        self.__controladorJogo = ControladorJogo.ControladorJogo(sistema)
        self.__controladorVenda = ControladorVendas.ControladorVendas(sistema)
        self.__controladorDesenvolvedora = ControladorDesenvolvedora.ControladorDesenvolvedora(sistema)
        self.__controladorTransportadora = ControladorTransportadora.ControladorTransportadora(sistema)
        self.__controladorUsuario = ControladorUsuario.ControladorUsuario(sistema)

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

    # Listar todos as Desenvolvedoras cadastrados.
    def listarDesenvolvedoras(self):
        content = []
        desenvolvedoras = self.__controladorDesenvolvedora.recuperarDesenvolvedoras()
        desenvolvedoras = Iterator.Iterator(desenvolvedoras)

        for desenvolvedora in desenvolvedoras:
            content.push(str(desenvolvedora))

        return content

    # Listar as Desenvolvedoras que tiveram mais jogos vendidos.
    def listarDesenvolvedorasMaisJogosVendidos(self):
        content = ''
        aux = []
        vendas = self.__controladorVenda.recuperarVendas()
        vendas = Iterator.Iterator(vendas)
        desenvolvedoras = self.__controladorDesenvolvedora.recuperarDesenvolvedoras()
        desenvolvedoras = Iterator.Iterator(desenvolvedoras)
        jogos = self.__controladorJogo.recuperarJogos()
        jogos = Iterator.Iterator(jogos)

        arr_nome = []
        vendas_arr = []
        for desenvolvedora in desenvolvedoras:
            vendas_arr.append(0)
            arr_nome.append(desenvolvedora.nome)
        dict_desenvolv = {"Desenvolvedora": arr_nome, "Jogos Vendidos": vendas_arr}

        for venda in vendas:
            itens = venda.itensVenda
            if isinstance(itens, list):
                itens = Iterator.Iterator(itens)
                for item in itens:
                    for jogo in jogos:
                        if item.codigoProduto.codigo == jogo.codigo:
                            indice = dict_desenvolv["Desenvolvedora"].index(jogo.desenvolvedora.nome)
                            dict_desenvolv['Jogos Vendidos'][indice] += 1
            else:
                for jogo in jogos:
                    if itens.codigoProduto.codigo == jogo.codigo:
                        indice = dict_desenvolv["Desenvolvedora"].index(jogo.desenvolvedora.nome)
                        dict_desenvolv['Jogos Vendidos'][indice] += 1

            # Ordenacao para listar as desenvolvedoras com mais jogos vendidos
            desenvolvedoras_jogos_vendidos = list(zip(dict_desenvolv["Desenvolvedora"], dict_desenvolv["Jogos Vendidos"]))
            desenvolvedoras_jogos_vendidos_sorted = sorted(desenvolvedoras_jogos_vendidos, key=lambda x: x[1],reverse=True)

        for i in range(len(desenvolvedoras_jogos_vendidos_sorted)):
            aux.append(desenvolvedoras_jogos_vendidos_sorted[i])

        for i in range(len(aux)):
            for desenvolvedora in desenvolvedoras:
                if desenvolvedora.nome == aux[i][0]:
                    content += desenvolvedora.__str__() + " - Vendas - " + str(aux[i][1]) + "\n"

        return content

    # Listar as Desenvolvedoras que tiveram o maior valor (lucro) de Jogos vendidos.
    def listarDesenvolvedorasMaisLucro(self):
        content = ''
        aux = []
        vendas = self.__controladorVenda.recuperarVendas()
        desenvolvedoras = self.__controladorDesenvolvedora.recuperarDesenvolvedoras()
        desenvolvedoras = Iterator.Iterator(desenvolvedoras)
        jogos = self.__controladorJogo.recuperarJogos()
        jogos = Iterator.Iterator(jogos)
        vendas = Iterator.Iterator(vendas)

        arr_nome = []
        saldo_null = []
        for desenvolvedora in desenvolvedoras:
            saldo_null.append(0)
            arr_nome.append(desenvolvedora.nome)

        dict_desenvolv = {"Desenvolvedora": arr_nome, "Lucro": saldo_null}

        for venda in vendas:
            itens = venda.itensVenda
            if isinstance(itens, list):
                itens = Iterator.Iterator(itens)
                for item in itens:
                    for jogo in jogos:
                        if item.codigoProduto.codigo == jogo.codigo:
                            indice = dict_desenvolv["Desenvolvedora"].index(jogo.desenvolvedora.nome)
                            dict_desenvolv['Lucro'][indice] += jogo.valor
            else:
                for jogo in jogos:
                    if itens.codigoProduto.codigo == jogo.codigo:
                        indice = dict_desenvolv["Desenvolvedora"].index(jogo.desenvolvedora.nome)
                        dict_desenvolv['Lucro'][indice] += jogo.valor

        desenvolvedoras_lucro = list(zip(dict_desenvolv["Desenvolvedora"], dict_desenvolv["Lucro"]))
        desenvolvedoras_lucro_sorted = sorted(desenvolvedoras_lucro, key=lambda x: x[1], reverse=True)

        for i in range(len(desenvolvedoras_lucro_sorted)):
            aux.append(desenvolvedoras_lucro_sorted[i])

        for i in range(len(aux)):
            for desenvolvedora in desenvolvedoras:
                if desenvolvedora.nome == aux[i][0]:
                    content += desenvolvedora.__str__() + " - Lucro - " + str(aux[i][1]) + "\n"

        return content


    # Listar todas as Transportadoras
    def listarTransportadoras(self):
        content = ''
        transportadoras = self.__controladorTransportadora.recuperarTransportadoras()
        transportadoras = Iterator.Iterator(transportadoras)
        for transportadora in transportadoras:
            content += transportadora.__str__() + "\n"

        return content


    # Listar todos os Gerentes cadastrados.
    def listarGerentes(self):
        content = ''
        gerentes = self.__controladorUsuario.recuperarGerentes()
        gerentes = Iterator.Iterator(gerentes)
        for gerente in gerentes:
            content += gerente.__str__() + '\n'

        return content


    #Listar todos os Clientes cadastrados, sejam eles Épicos ou não.
    def listarClientes(self):
        content = ''
        clientes = self.__controladorUsuario.recuperarClientes()
        clientes = Iterator.Iterator(clientes)
        for cliente in clientes:
            print(cliente.clienteEpico)
            content += cliente.__str__() + '\n'

        return content


    #Listar todos os Clientes Épicos cadastrados.
    def listarClientesEpicos(self):
        content = ''
        clientes = self.__controladorUsuario.recuperarClientes()
        clientes = Iterator.Iterator(clientes)
        for cliente in clientes:
            if cliente.clienteEpico:
                content += cliente.__str__() + '\n'

        return content


    # Listar os dez Clientes com maior nível na plataforma.
    def listarDezClientesMaiorNivel(self):
        content = ''
        clientes = self.__controladorUsuario.recuperarClientes()
        clientes = Iterator.Iterator(clientes)
        clientes_nivel = []
        for cliente in clientes:
            clientes_nivel.append(cliente)

        clientes_nivel = sorted(clientes_nivel, key=lambda x: x.nivel, reverse=True)

        for i in range(min(10, len(clientes_nivel))):
            content += clientes_nivel[i].__str__() + '\n'

        return content


    # Listar o histórico de Vendas de um Cliente em específico.
    def listarHistoricoVendasCliente(self, clienteCodigo):
        vendas = self.__controladorVenda.recuperarVendas()
        vendas = Iterator.Iterator(vendas)
        content = ''
        for venda in vendas:
            if venda.cliente.codigo == clienteCodigo:
                content += venda.__str__() + '\n'

        return content


    # Listar todas as Vendas realizadas.
    def todasVendas(self):
        vendas = self.__controladorVenda.recuperarVendas()
        vendas = Iterator.Iterator(vendas)
        content = ''
        for venda in vendas:
            content += venda.__str__() + '\n'

        return content


    # Listar Vendas realizadas em um mês em específico e o total de lucro gerado no mês.
    def listarVendasLucroMes(self, mes):
        vendas = self.__controladorVenda.recuperarVendas()
        produtos = self.__controladorJogo.recuperarJogos()

        lucro = 0
        conteudo = ''

        vendas = Iterator.Iterator(vendas)
        produtos = Iterator.Iterator(produtos)

        for venda in vendas:
            if venda.dataVenda.month == mes:
                itens = venda.itensVenda
                if isinstance(itens, list):
                    itens = Iterator.Iterator(itens)
                    for item in itens:
                        lucro += item.calcularTotal()
                        conteudo += venda.__str__() + '\n'
                else:
                    lucro = lucro + itens.calcularTotal()
                    conteudo += venda.__str__() + '\n'

        conteudo += "Lucro total gerado: " + str(lucro)
        return conteudo


    # Listar Vendas de uma Desenvolvedora especifica realizadas em um mês em
    # específico e o total de lucro gerado no mês para a Desenvolvedora.
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

                            if item.codigoProduto.codigo == produto.codigo:
                                if produto.desenvolvedora.nome == desenvolvedora:
                                    lucro = lucro + item.calcularTotal()
                                    conteudo += venda.__str__() + '\n'
                else:
                    for produto in produtos:
                        if itens.codigoProduto.codigo == produto.codigo:
                            if produto.desenvolvedora.nome == desenvolvedora:
                                lucro = lucro + itens.calcularTotal()
                                conteudo += venda.__str__() + '\n'

        conteudo += "Lucro total gerado: " + str(lucro)
        return conteudo

    # Listar todas as Vendas pagas em Boleto.
    def listarVendasPorBoleto(self):
        vendas = self.__controladorVenda.recuperarVendas()
        vendas = Iterator.Iterator(vendas)
        content = ''
        for venda in vendas:
            pagamento = venda.formaPagamento
            if isinstance(pagamento, Pagamento.Boleto):
                content += venda.__str__() + '\n'

        return content


    # Listar todas as Vendas pagas com Cartão de Crédito.
    def listarVendasPorCartaoCredito(self):
        vendas = self.__controladorVenda.recuperarVendas()
        vendas = Iterator.Iterator(vendas)
        content = ''
        for venda in vendas:
            pagamento = venda.formaPagamento
            if isinstance(pagamento, Pagamento.CartaoCredito):
                content += venda.__str__() + '\n'

        return content


    # Listar todas as Vendas pagas com PIX.
    def listarVendasPorPix(self):
        vendas = self.__controladorVenda.recuperarVendas()
        vendas = Iterator.Iterator(vendas)
        content = ''
        for venda in vendas:
            pagamento = venda.formaPagamento
            if isinstance(pagamento, Pagamento.Pix):
                content += venda.__str__() + '\n'

        return content

