import PySimpleGUI as sg
from datetime import datetime
from views import geradorTelas
from controllers import ControladorDesenvolvedora, ControladorJogo, ControladorRelatorios, ControladorTransportadora, ControladorUsuario, ControladorVendas
from models import Pagamento, Jogo
def validar_data(data):
    try:
        datetime.strptime(data, '%d/%m/%Y')
        return True
    except ValueError:
        return False

def validarGerente(values, controlador):
    for campo, valor in values.items():
        if valor == '':
            sg.popup('Todos os campos devem ser preenchidos')
            return False
    for campo, valor in values.items():
        if campo == 'cpf' and not valor.isdigit():
            sg.popup('CPF deve conter apenas números')
            return False
        elif campo == 'rg' and not valor.isdigit():
            sg.popup('RG deve conter apenas números')
            return False
        elif campo == 'salario' and not valor.isdigit():
            sg.popup('Salário deve conter apenas números')
            return False
        elif campo == 'pis' and not valor.isdigit():
            sg.popup('PIS deve conter apenas números')
            return False
        elif campo == 'codigo' and not valor.isdigit():
            sg.popup('Código deve conter apenas números')
            return False
        elif campo == 'codigo':
            gerente = controlador.recuperarGerente(valor)
            if gerente is not None:
                sg.popup('Código já cadastrado')
                return False
        elif campo == 'dataNascimento':
            if not validar_data(valor):
                sg.popup_error('A data de nascimento é inválida. Use o formato DD/MM/AAAA.')
                return False
        elif campo == 'dataAdmissao':
            if not validar_data(valor):
                sg.popup_error('A data de admissão é inválida. Use o formato DD/MM/AAAA.')
                return False
    return True

def validarCliente(values, controlador):
    for campo, valor in values.items():
        if valor == '':
            sg.popup('Todos os campos devem ser preenchidos')
            return False
    for campo, valor in values.items():
        if campo == 'cpf' and not valor.isdigit():
            sg.popup('CPF deve conter apenas números')
            return False
        elif campo == 'rg' and not valor.isdigit():
            sg.popup('RG deve conter apenas números')
            return False
        elif campo == 'codigo' and not valor.isdigit():
            sg.popup('Código deve conter apenas números')
            return False
        elif campo == 'codigo':
            cliente = controlador.recuperarCliente(valor)
            if cliente is not None:
                sg.popup('Código já cadastrado')
                return False
        elif campo == 'dataNascimento':
            if not validar_data(valor):
                sg.popup_error('A data de nascimento é inválida. Use o formato DD/MM/AAAA.')
                return False
        elif campo == 'dataCadastro':
            if not validar_data(valor):
                sg.popup_error('A data de cadastro é inválida. Use o formato DD/MM/AAAA.')
                return False
    return True

def validarDesenvolvedora(values, controlador):
    for campo, valor in values.items():
        if valor == '':
            sg.popup('Todos os campos devem ser preenchidos')
            return False
    for campo, valor in values.items():
        if campo == 'cnpj' and not valor.isdigit():
            sg.popup('CNPJ deve conter apenas números')
            return False
        elif campo == 'codigo' and not valor.isdigit():
            sg.popup('Código deve conter apenas números')
            return False
        elif campo == 'codigo':
            desenvolvedora = controlador.recuperarDesenvolvedora(valor)
            if desenvolvedora is not None:
                sg.popup('Código já cadastrado')
                return False
    return True

def validarTransportadora(values, controlador):
    for campo, valor in values.items():
        if valor == '':
            sg.popup('Todos os campos devem ser preenchidos')
            return False
    for campo, valor in values.items():
        if campo == 'cnpj' and not valor.isdigit():
            sg.popup('CNPJ deve conter apenas números')
            return False
        elif campo == 'codigo' and not valor.isdigit():
            sg.popup('Código deve conter apenas números')
            return False
        elif campo == 'codigo':
            transportadora = controlador.recuperarTransportadora(valor)
            if transportadora is not None:
                sg.popup('Código já cadastrado')
                return False
    return True

def validarPagamentoBoletos(values, controlador):
    for campo, valor in values.items():
        if valor == '':
            sg.popup('Todos os campos devem ser preenchidos')
            return False
    for campo, valor in values.items():
        if campo == 'codigo' and not valor.isdigit():
            sg.popup('Código deve conter apenas números')
            return False
        elif campo == 'codigo':
            pagamento = controlador.recuperarPagamento(valor, "Boleto")
            if pagamento is not None:
                sg.popup('Código já cadastrado')
                return False
    return True

def validarPagamentoCartaoCredito(values, controlador):
    for campo, valor in values.items():
        if valor == '':
            sg.popup('Todos os campos devem ser preenchidos')
            return False
    for campo, valor in values.items():
        if campo == 'codigo' and not valor.isdigit():
            sg.popup('Código deve conter apenas números')
            return False
        elif campo == 'codigo':
            pagamento = controlador.recuperarPagamento(valor, "CartaoCredito")
            if pagamento is not None:
                sg.popup('Código já cadastrado')
                return False
    return True

def validarPagamentoPix(values, controlador):
    for campo, valor in values.items():
        if valor == '':
            sg.popup('Todos os campos devem ser preenchidos')
            return False
    for campo, valor in values.items():
        if campo == 'codigo' and not valor.isdigit():
            sg.popup('Código deve conter apenas números')
            return False
        elif campo == 'codigo':
            pagamento = controlador.recuperarPagamento(valor, "PIX")
            if pagamento is not None:
                sg.popup('Código já cadastrado')
                return False
    return True

def validarJogo(values, controlador):
    for campo, valor in values.items():
        if valor == '':
            sg.popup('Todos os campos devem ser preenchidos')
            return False
    for campo, valor in values.items():
        if campo == 'codigo' and not valor.isdigit():
            sg.popup('Código deve conter apenas números')
            return False
        elif campo == 'codigo':
            jogo = controlador.recuperarJogo(valor)
            if jogo is not None:
                sg.popup('Código já cadastrado')
                return False
        elif campo == 'preco' and not valor.isdigit():
            sg.popup('Preço deve conter apenas números')
            return False
        elif campo == 'dataLancamento':
            if not validar_data(valor):
                sg.popup_error('A data de lançamento é inválida. Use o formato DD/MM/AAAA.')
                return False
    return True
def execucao(sistema):

    controlador_desenvolvedora = ControladorDesenvolvedora.ControladorDesenvolvedora(sistema)
    controlador_transportadora = ControladorTransportadora.ControladorTransportadora(sistema)
    controlador_jogo = ControladorJogo.ControladorJogo(sistema)
    controlador_usuario = ControladorUsuario.ControladorUsuario(sistema)
    controlador_vendas = ControladorVendas.ControladorVendas(sistema)
    controlador_relatorios = ControladorRelatorios.ControladorRelatorios(sistema)

    window = geradorTelas.createWindow('inicial', sistema)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == 'cancelar':
            break

        elif event == 'cadastrarGerente':


            window_gerente = geradorTelas.createWindow('cadastrarGerente', sistema)

            while True:
                event_gerente, values_gerente = window_gerente.read()
                if event_gerente == sg.WIN_CLOSED or event_gerente == 'cancelar':
                    break
                elif event_gerente == 'salvarGerente':
                    if validarGerente(values_gerente, controlador_usuario):
                        gerente = controlador_usuario.criarGerente(values_gerente['codigo'], values_gerente['nome'], values_gerente['cpf'], values_gerente['rg'], values_gerente['dataNascimento'], values_gerente['endereco'], values_gerente['cep'], values_gerente['email'], values_gerente['salario'], values_gerente['pis'], values_gerente['dataAdmissao'])
                        controlador_usuario.inserirGerente(gerente)
                        sg.popup("Gerente cadastrado com sucesso!")

            window_gerente.close()

        elif event == 'cadastrarCliente':


            window_cliente = geradorTelas.createWindow('cadastrarCliente', sistema)

            while True:
                event_cliente, values_cliente = window_cliente.read()
                if event_cliente == sg.WIN_CLOSED or event_cliente == 'cancelar':
                    break
                elif event_cliente == 'salvarCliente':
                    if validarCliente(values_cliente, controlador_usuario):
                        if values_cliente['simEpico']:
                            epico = 1
                        else:
                            epico = 0
                        cliente = controlador_usuario.criarCliente(values_cliente['codigo'], values_cliente['nome'], values_cliente['cpf'], values_cliente['rg'], values_cliente['dataNascimento'], values_cliente['endereco'], values_cliente['cep'], values_cliente['email'], values_cliente['dataCadastro'], values_cliente['nivel'], epico, None)
                        controlador_usuario.inserirCliente(cliente)
                        sg.popup("Cliente cadastrado com sucesso!")
            window_cliente.close()

        elif event == 'cadastrarDesenvolvedora':


            window_desenvolvedora = geradorTelas.createWindow('cadastrarDesenvolvedora', sistema)

            while True:
                event_desenvolvedora, values_desenvolvedora = window_desenvolvedora.read()
                if event_desenvolvedora == sg.WIN_CLOSED or event_desenvolvedora == 'cancelar':
                    break
                elif event_desenvolvedora == 'salvarDesenvolvedora':
                    if validarDesenvolvedora(values_desenvolvedora, controlador_desenvolvedora):
                        desenvolvedora = controlador_desenvolvedora.criarDesenvolvedora(values_desenvolvedora['codigo'], values_desenvolvedora['cnpj'], values_desenvolvedora['nome'], values_desenvolvedora['email'], values_desenvolvedora['site'], values_desenvolvedora['redeSocial'], values_desenvolvedora['endereco'])
                        controlador_desenvolvedora.inserirDesenvolvedora(desenvolvedora)
                        sg.popup("Desenvolvedora cadastrada com sucesso!")

            window_desenvolvedora.close()


        elif event == 'cadastrarTransportadora':


            window_transportadora = geradorTelas.createWindow('cadastrarTransportadora', sistema)

            while True:
                event_transportadora, values_transportadora = window_transportadora.read()
                if event_transportadora == sg.WIN_CLOSED or event_transportadora == 'cancelar':
                    break
                elif event_transportadora == 'salvarTransportadora':
                    if validarTransportadora(values_transportadora, controlador_transportadora):
                        transportadora = controlador_transportadora.criarTransportadora(values_transportadora['codigo'], values_transportadora['cnpj'], values_transportadora['nome'], values_transportadora['email'], values_transportadora['telefone'], values_transportadora['endereco'], values_transportadora['tempoEntrega'])
                        controlador_transportadora.inserirTransportadora(transportadora)
                        sg.popup("Transportadora cadastrada com sucesso!")

            window_transportadora.close()


        elif event == 'cadastrarJogo':


            window_jogo = geradorTelas.createWindow('cadastrarJogo', sistema)

            while True:
                event_jogo, values_jogo = window_jogo.read()
                if event_jogo == sg.WIN_CLOSED or event_jogo == 'cancelar':
                    break
                elif event_jogo == 'salvarJogo':
                    if validarJogo(values_jogo, controlador_jogo):
                        desenvolvedora = controlador_desenvolvedora.recuperarDesenvolvedora(values_jogo['comboDesenvolvedora'][0])

                        if values_jogo['simDisponivel']:
                            disponivel = 1
                        else:
                            disponivel = 0

                        if values_jogo['acao']:
                            genero = 'Acao'
                        elif values_jogo['aventura']:
                            genero = 'Aventura'
                        elif values_jogo['corrida']:
                            genero = 'Corrida'
                        elif values_jogo['esporte']:
                            genero = 'Esporte'
                        elif values_jogo['rpg']:
                            genero = 'RPG'

                        jogo = controlador_jogo.criarJogo(genero, values_jogo['codigo'], values_jogo['nome'], values_jogo['descricao'], desenvolvedora, values_jogo['dataLancamento'], values_jogo['valor'], values_jogo['requisitosMinimos'], values_jogo['avaliacao'], values_jogo['comentarios'], disponivel)
                        controlador_jogo.inserirJogo(jogo)
                        sg.popup("Jogo cadastrado com sucesso!")


            window_jogo.close()

        elif event == 'cadastrarVenda':


            window_venda = geradorTelas.createWindow('cadastrarVenda', sistema)

            while True:
                event_venda, values_venda = window_venda.read()
                if event_venda == sg.WIN_CLOSED or event_venda == 'cancelar':
                    break
                elif event_venda == 'adicionarItem':
                    jogo = controlador_jogo.recuperarJogo(values_venda['comboProduto'][0])

                    novo_item = [values_venda['novoCodigo'], values_venda['comboProduto'], str(jogo.valor), values_venda['novoQuantidade']]
                    itens_venda = window_venda['tabelaItensVenda'].get()
                    itens_venda.append(novo_item)
                    window_venda['tabelaItensVenda'].update(values=itens_venda)
                    window_venda['novoCodigo'].update(value='')
                    window_venda['comboProduto'].update(value='')
                    window_venda['novoQuantidade'].update(value='')

                elif event_venda == 'salvarVenda':
                    cliente = controlador_usuario.recuperarCliente(values_venda['comboCliente'][0])
                    if values_venda['boleto']:
                        if cliente.pagamento is None or type(cliente.pagamento).__name__ == 'Boleto':
                            window_boletos = geradorTelas.createWindow('boleto', sistema)
                            while True:
                                event_boleto, values_boleto = window_boletos.read()
                                if event_boleto == sg.WIN_CLOSED or event_boleto == 'cancelar':
                                    break
                                elif event_boleto == 'salvar':
                                    if validarPagamentoBoletos(values_boleto, controlador_vendas):
                                        pagamento = Pagamento.Boleto(values_boleto['codigo'], values_boleto['numero'])
                                        cliente.pagamento = pagamento
                                        controlador_usuario.atualizarCliente(cliente)
                                        break
                            window_boletos.close()
                    elif values_venda['cartaoCredito']:
                        if cliente.pagamento is None or type(cliente.pagamento).__name__ == 'CartaoCredito':
                            window_cartao = geradorTelas.createWindow('cartaoCredito', sistema)
                            while True:
                                event_cartao, values_cartao = window_cartao.read()
                                if event_cartao == sg.WIN_CLOSED or event_cartao == 'cancelar':
                                    break
                                elif event_cartao == 'salvar':
                                    if validarPagamentoCartaoCredito(values_cartao, controlador_vendas):
                                        pagamento = Pagamento.CartaoCredito(values_cartao['codigo'], values_cartao['nome'], values_cartao['bandeira'], values_cartao['numero'])
                                        cliente.pagamento = pagamento
                                        controlador_usuario.atualizarCliente(cliente)
                                        break
                            window_cartao.close()

                    elif values_venda['pix']:
                        if cliente.pagamento is None or type(cliente.pagamento).__name__ == 'Pix':
                            window_pix = geradorTelas.createWindow('pix', sistema)
                            while True:
                                event_pix, values_pix = window_pix.read()
                                if event_pix == sg.WIN_CLOSED or event_pix == 'cancelar':
                                    break
                                elif event_pix == 'salvar':
                                    if validarPagamentoPix(values_pix, controlador_vendas):
                                        pagamento = Pagamento.Pix(values_pix['codigo'], values_pix['chave'])
                                        cliente.pagamento = pagamento
                                        controlador_usuario.atualizarCliente(cliente)
                                        break
                            window_pix.close()
                    itens_venda = window_venda['tabelaItensVenda'].get()
                    itens = []
                    for item in itens_venda:
                        jogo = controlador_jogo.recuperarJogo(item[1][0])
                        itens.append(controlador_vendas.criarItemVenda(item[0], jogo.codigo, item[2], item[3]))

                    for item in itens:
                        controlador_vendas.inserirItemVenda(item)

                    gerente = controlador_usuario.recuperarGerente(values_venda['comboGerente'][0])
                    transportadora = controlador_transportadora.recuperarTransportadora(values_venda['comboTransportadora'][0])
                    pagamento = cliente.pagamento
                    itens_fisicos = 0
                    if values_venda['simPossui']:
                        itens_fisicos = 1
                    venda = controlador_vendas.criarVenda(values_venda['codigo'], cliente, gerente, values_venda['dataVenda'], 0, itens, itens_fisicos, 0, 0, pagamento, transportadora)
                    controlador_vendas.inserirVenda(venda)
                    sg.popup("Venda cadastrada com sucesso!")




            window_venda.close()

        elif event == 'relatorios':

            window_relatorio = geradorTelas.createWindow('relatorios', sistema)

            while True:
                event_relatorio, values_relatorio = window_relatorio.read()
                if event_relatorio == sg.WIN_CLOSED or event_relatorio == 'cancelar':
                    break
                elif event_relatorio == 'enviarRelatorio':
                    window_relatorio['relatorio'].update(value='')

                    try:
                        if values_relatorio['comboRelatorios'] == 'Listar todos os Jogos cadastrados.':
                            window_relatorio['relatorio'].update(value=controlador_relatorios.listarJogos(Jogo.Jogo))
                        if values_relatorio['comboRelatorios'] == 'Listar todos os Jogos da categoria Ação.':
                            window_relatorio['relatorio'].update(value=controlador_relatorios.listarJogos(Jogo.Acao))
                        if values_relatorio['comboRelatorios'] == 'Listar todos os Jogos da categoria Aventura.':
                            window_relatorio['relatorio'].update(value=controlador_relatorios.listarJogos(Jogo.Aventura))
                        if values_relatorio['comboRelatorios'] == 'Listar todos os Jogos da categoria RPG.':
                            window_relatorio['relatorio'].update(value=controlador_relatorios.listarJogos(Jogo.RPG))
                        if values_relatorio['comboRelatorios'] == 'Listar todos os Jogos da categoria Esporte.':
                            window_relatorio['relatorio'].update(value=controlador_relatorios.listarJogos(Jogo.Esporte))
                        if values_relatorio['comboRelatorios'] == 'Listar todos os Jogos da categoria Corrida.':
                            window_relatorio['relatorio'].update(value=controlador_relatorios.listarJogos(Jogo.Corrida))
                        if values_relatorio['comboRelatorios'] == 'Listar os dez Jogos mais caros':
                            window_relatorio['relatorio'].update(value=controlador_relatorios.listarJogosMaisCaros())
                        if values_relatorio['comboRelatorios'] == 'Listar os dez Jogos mais baratos':
                            window_relatorio['relatorio'].update(value=controlador_relatorios.listarJogosMaisBaratos())
                        if values_relatorio['comboRelatorios'] == 'Listar todos os Jogos ordenados de forma crescente por nota de avaliação (A)':
                            window_relatorio['relatorio'].update(value=controlador_relatorios.listarJogoPorAvaliacao('A'))
                        if values_relatorio['comboRelatorios'] == 'Listar todos os Jogos ordenados de forma crescente por nota de avaliação (B)':
                            window_relatorio['relatorio'].update(value=controlador_relatorios.listarJogoPorAvaliacao('B'))
                        if values_relatorio['comboRelatorios'] == 'Listar todos as Desenvolvedoras cadastrados.':
                            window_relatorio['relatorio'].update(value=controlador_relatorios.listarDesenvolvedoras())
                        if values_relatorio['comboRelatorios'] == 'Listar as Desenvolvedoras que tiveram mais jogos vendidos.':
                            window_relatorio['relatorio'].update(value=controlador_relatorios.listarDesenvolvedorasMaisJogosVendidos())
                        if values_relatorio['comboRelatorios'] == 'Listar as Desenvolvedoras que tiveram o maior valor (lucro) de Jogos vendidos.':
                            window_relatorio['relatorio'].update(value=controlador_relatorios.listarDesenvolvedorasMaisLucro())
                        if values_relatorio['comboRelatorios'] == 'Listar todas as Transportadoras':
                            window_relatorio['relatorio'].update(value=controlador_relatorios.listarTransportadoras())
                        if values_relatorio['comboRelatorios'] == 'Listar todos os Gerentes cadastrados.':
                            window_relatorio['relatorio'].update(value=controlador_relatorios.listarGerentes())
                        if values_relatorio['comboRelatorios'] == 'Listar todos os Clientes cadastrados.':
                            window_relatorio['relatorio'].update(value=controlador_relatorios.listarClientes())
                        if values_relatorio['comboRelatorios'] == 'Listar todos os Clientes Épicos cadastrados.':
                            window_relatorio['relatorio'].update(value=controlador_relatorios.listarClientesEpicos())
                        if values_relatorio['comboRelatorios'] == 'Listar os dez Clientes com maior nível na plataforma.':
                            window_relatorio['relatorio'].update(value=controlador_relatorios.listarDezClientesMaiorNivel())
                        if values_relatorio['comboRelatorios'] == 'Listar o histórico de Vendas de um Cliente em específico.':
                            window_relatorio['relatorio'].update(value=controlador_relatorios.listarHistoricoVendasCliente(int(values_relatorio['comboCliente'][0])))
                        if values_relatorio['comboRelatorios'] == 'Listar todas as Vendas realizadas.':
                            window_relatorio['relatorio'].update(value=controlador_relatorios.todasVendas())
                        if values_relatorio['comboRelatorios'] == 'Listar Vendas realizadas em um mês em específico e o total de lucro gerado no mês.':
                            window_relatorio['relatorio'].update(value=controlador_relatorios.listarVendasLucroMes(int(values_relatorio['comboMes'])))
                        if values_relatorio['comboRelatorios'] == 'Listar Vendas de uma Desenvolvedora especifica realizadas em um mês em específico e o total de lucro gerado no mês':
                            window_relatorio['relatorio'].update(value=controlador_relatorios.listarVendasLucroDesenvolvedora(int(values_relatorio['comboMes']), int(values_relatorio['comboDesenvolvedora'][0])))
                        if values_relatorio['comboRelatorios'] == 'Listar todas as Vendas pagas em Boleto.':
                            window_relatorio['relatorio'].update(value=controlador_relatorios.listarVendasPorBoleto())
                        if values_relatorio['comboRelatorios'] == 'Listar todas as Vendas pagas com Cartão de Crédito.':
                            window_relatorio['relatorio'].update(value=controlador_relatorios.listarVendasPorCartaoCredito())
                        if values_relatorio['comboRelatorios'] == 'Listar todas as Vendas pagas com PIX.':
                            window_relatorio['relatorio'].update(value=controlador_relatorios.listarVendasPorPix())
                    except:
                        sg.popup("Relatório")
            window_relatorio.close()

        elif event == 'alterarJogo':
            pass

    window.close()
