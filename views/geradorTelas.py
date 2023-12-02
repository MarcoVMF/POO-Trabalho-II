import PySimpleGUI as sg
from controllers import ControladorDesenvolvedora, ControladorUsuario, ControladorTransportadora, ControladorJogo


def createWindow(type, sistema):
    sg.theme('DarkAmber')
    frame_size = (800, 800)
    espaco = (20, 0)
    popup_location = (125, 0)


    if type == 'cadastrarGerente':
        cadastroGerente = \
            [
                [sg.Text('Código: ', font=('Verdana', 10, 'bold'), size=espaco),
                 sg.InputText(size=(20, 0), key='codigo')],
                [sg.Text('Nome: ', font=('Verdana', 10, 'bold'), size=espaco),
                 sg.InputText(size=(20, 0), key='nome')],
                [sg.Text('CPF: ', font=('Verdana', 10, 'bold'), size=espaco),
                 sg.InputText(size=(20, 0), key='cpf')],
                [sg.Text('RG: ', font=('Verdana', 10, 'bold'), size=espaco),
                 sg.InputText(size=(20, 0), key='rg')],
                [sg.Text('Data de Nascimento: ', font=('Verdana', 10, 'bold'), size=espaco),
                 sg.InputText(size=(20, 0), key='dataNascimento')],
                [sg.Text('Endereço: ', font=('Verdana', 10, 'bold'), size=espaco),
                 sg.InputText(size=(20, 0), key='endereco')],
                [sg.Text('CEP: ', font=('Verdana', 10, 'bold'), size=espaco),
                 sg.InputText(size=(20, 0), key='cep')],
                [sg.Text('E-Mail: ', font=('Verdana', 10, 'bold'), size=espaco),
                 sg.InputText(size=(20, 0), key='email')],
                [sg.Text('Salário: ', font=('Verdana', 10, 'bold'), size=espaco),
                 sg.InputText(size=(20, 0), key='salario')],
                [sg.Text('PIS: ', font=('Verdana', 10, 'bold'), size=espaco),
                 sg.InputText(size=(20, 0), key='pis')],
                [sg.Text('Data de Admissão: ', font=('Verdana', 10, 'bold'), size=espaco),
                 sg.InputText(size=(20, 0), key='dataAdmissao')],
                [sg.Text('Não é possível fechar o programa durante o cadastro!', text_color='red')],
                [sg.Button('Salvar', key='salvarGerente', size=(15, 1)),
                 sg.Button('Cancelar', key='cancelar', size=(15, 1))]
            ]
        return sg.Window('Cadastro de Gerente', cadastroGerente, finalize=True,
                         relative_location=popup_location, element_justification='c', no_titlebar=True,
                         grab_anywhere=False, modal=True)

    elif type == 'cadastrarCliente':
        cadastroCliente = \
            [
                [sg.Text('Código: ', font=('Verdana', 10, 'bold'), size=espaco),
                 sg.InputText(size=(20, 0), key='codigo')],
                [sg.Text('Nome: ', font=('Verdana', 10, 'bold'), size=espaco),
                 sg.InputText(size=(20, 0), key='nome')],
                [sg.Text('CPF: ', font=('Verdana', 10, 'bold'), size=espaco),
                 sg.InputText(size=(20, 0), key='cpf')],
                [sg.Text('RG: ', font=('Verdana', 10, 'bold'), size=espaco),
                 sg.InputText(size=(20, 0), key='rg')],
                [sg.Text('Data de Nascimento: ', font=('Verdana', 10, 'bold'), size=espaco),
                 sg.InputText(size=(20, 0), key='dataNascimento')],
                [sg.Text('Endereço: ', font=('Verdana', 10, 'bold'), size=espaco),
                 sg.InputText(size=(20, 0), key='endereco')],
                [sg.Text('CEP: ', font=('Verdana', 10, 'bold'), size=espaco),
                 sg.InputText(size=(20, 0), key='cep')],
                [sg.Text('E-Mail: ', font=('Verdana', 10, 'bold'), size=espaco),
                 sg.InputText(size=(20, 0), key='email')],
                [sg.Text('Data de Cadastro: ', font=('Verdana', 10, 'bold'), size=espaco),
                 sg.InputText(size=(20, 0), key='dataCadastro')],
                [sg.Text('Nível: ', font=('Verdana', 10, 'bold'), size=espaco),
                 sg.InputText(size=(20, 0), key='nivel')],
                [sg.Text('Cliente épico: ', font=('Verdana', 10, 'bold'), size=espaco),
                 sg.Radio('Sim', 'clienteEpico', key='simEpico'), sg.Radio('Não', 'clienteEpico', key='naoEpico')],
                [sg.Text('Não é possível fechar o programa durante o cadastro!', text_color='red')],
                [sg.Button('Salvar', key='salvarCliente', size=(15, 1)),
                 sg.Button('Cancelar', key='cancelar', size=(15, 1))]
            ]
        return sg.Window('Cadastro de Cliente', cadastroCliente, finalize=True, size=frame_size,
                         relative_location=popup_location, element_justification='c', no_titlebar=True,
                         grab_anywhere=False, modal=True)

    elif type == 'cadastrarDesenvolvedora':
        cadastroDesenvolvedora = \
            [
                [sg.Text('Código: ', font=('Verdana', 10, 'bold'), size=espaco),
                 sg.InputText(size=(20, 0), key='codigo')],
                [sg.Text('CNPJ: ', font=('Verdana', 10, 'bold'), size=espaco),
                 sg.InputText(size=(20, 0), key='cnpj')],
                [sg.Text('Nome: ', font=('Verdana', 10, 'bold'), size=espaco),
                 sg.InputText(size=(20, 0), key='nome')],
                [sg.Text('E-Mail: ', font=('Verdana', 10, 'bold'), size=espaco),
                 sg.InputText(size=(20, 0), key='email')],
                [sg.Text('Site: ', font=('Verdana', 10, 'bold'), size=espaco),
                 sg.InputText(size=(20, 0), key='site')],
                [sg.Text('Rede Social: ', font=('Verdana', 10, 'bold'), size=espaco),
                 sg.InputText(size=(20, 0), key='redeSocial')],
                [sg.Text('Endereço: ', font=('Verdana', 10, 'bold'), size=espaco),
                 sg.InputText(size=(20, 0), key='endereco')],
                [sg.Text('Não é possível fechar o programa durante o cadastro!', text_color='red')],
                [sg.Button('Salvar', key='salvarDesenvolvedora', size=(15, 1)),
                 sg.Button('Cancelar', key='cancelar', size=(15, 1))]
            ]
        return sg.Window('Cadastro de Desenvolvedora', cadastroDesenvolvedora, finalize=True, size=frame_size,
                         relative_location=popup_location, element_justification='c', no_titlebar=True,
                         grab_anywhere=False, modal=True)

    elif type == 'cadastrarTransportadora':
        cadastroTransportadora = \
            [
                [sg.Text('Código: ', font=('Verdana', 10, 'bold'), size=espaco),
                 sg.InputText(size=(20, 0), key='codigo')],
                [sg.Text('CNPJ: ', font=('Verdana', 10, 'bold'), size=espaco),
                 sg.InputText(size=(20, 0), key='cnpj')],
                [sg.Text('Nome: ', font=('Verdana', 10, 'bold'), size=espaco),
                 sg.InputText(size=(20, 0), key='nome')],
                [sg.Text('E-Mail: ', font=('Verdana', 10, 'bold'), size=espaco),
                 sg.InputText(size=(20, 0), key='email')],
                [sg.Text('Telefone: ', font=('Verdana', 10, 'bold'), size=espaco),
                 sg.InputText(size=(20, 0), key='telefone')],
                [sg.Text('Endereço: ', font=('Verdana', 10, 'bold'), size=espaco),
                 sg.InputText(size=(20, 0), key='endereco')],
                [sg.Text('Tempo de Entrega: ', font=('Verdana', 10, 'bold'), size=espaco),
                 sg.InputText(size=(20, 0), key='tempoEntrega')],
                [sg.Text('Não é possível fechar o programa durante o cadastro!', text_color='red')],
                [sg.Button('Salvar', key='salvarTransportadora', size=(15, 1)),
                 sg.Button('Cancelar', key='cancelar', size=(15, 1))]
            ]
        return sg.Window('Cadastro de Transportadora', cadastroTransportadora, finalize=True, size=frame_size,
                         relative_location=popup_location, element_justification='c', no_titlebar=True,
                         grab_anywhere=False, modal=True)

    elif type == 'cadastrarJogo':
        aux = []
        controlador_desenvolvedora = ControladorDesenvolvedora.ControladorDesenvolvedora(sistema)
        desenvolvedoras = controlador_desenvolvedora.recuperarDesenvolvedoras()
        for desenvolvedora in desenvolvedoras:
            aux.append(str(desenvolvedora.codigo) + "-" + desenvolvedora.nome)

        cadastroJogo = \
            [
                [sg.Text('Código: ', font=('Verdana', 10, 'bold'), size=espaco),
                 sg.InputText(size=(20, 0), key='codigo')],
                [sg.Text('Nome: ', font=('Verdana', 10, 'bold'), size=espaco),
                 sg.InputText(size=(20, 0), key='nome')],
                [sg.Text('Tipo: ', font=('Verdana', 10, 'bold'), size=espaco),
                 sg.Radio('Ação', 'tipo', key='acao'), sg.Radio('Aventura', 'tipo', key='aventura'),
                 sg.Radio('RPG', 'tipo', key='rpg'), sg.Radio('Esporte', 'tipo', key='esporte'),
                 sg.Radio('Corrida', 'tipo', key='corrida')],
                [sg.Text('Descrição: ', font=('Verdana', 10, 'bold'), size=espaco),
                 sg.InputText(size=(20, 0), key='descricao')],
                [sg.Text('Desenvolvedora: ', font=('Verdana', 10, 'bold'), size=espaco),
                    sg.Combo(aux, default_value='Selecione uma Desenvolvedora', key='comboDesenvolvedora', size=(100, 0))],
                [sg.Text('Data de Lançamento: ', font=('Verdana', 10, 'bold'), size=espaco),
                 sg.InputText(size=(20, 0), key='dataLancamento')],
                [sg.Text('Valor: ', font=('Verdana', 10, 'bold'), size=espaco),
                 sg.InputText(size=(20, 0), key='valor')],
                [sg.Text('Requisitos Mínimos: ', font=('Verdana', 10, 'bold'), size=espaco),
                 sg.InputText(size=(20, 0), key='requisitosMinimos')],
                [sg.Text('Avaliação: ', font=('Verdana', 10, 'bold'), size=espaco),
                 sg.Slider(range=(0, 5), orientation='h', key='avaliacao')],
                [sg.Text('Comentários: ', font=('Verdana', 10, 'bold'), size=espaco),
                 sg.InputText(size=(20, 0), key='comentarios')],
                [sg.Text('Disponível: ', font=('Verdana', 10, 'bold'), size=espaco),
                 sg.Radio('Sim', 'disponivel', key='simDisponivel'),
                 sg.Radio('Não', 'disponivel', key='naoDisponivel')],
                [sg.Text('Não é possível fechar o programa durante o cadastro!', text_color='red')],
                [sg.Button('Salvar', key='salvarJogo', size=(15, 1)),
                 sg.Button('Cancelar', key='cancelar', size=(15, 1))]
            ]
        return sg.Window('Cadastro de Jogo', cadastroJogo, finalize=True, size=frame_size,
                         relative_location=popup_location, element_justification='c', no_titlebar=True,
                         grab_anywhere=False, modal=True)

    elif type == 'cadastrarVenda':
        aux_cliente = []
        aux_gerente = []
        aux_transportadora = []
        aux_jogo = []

        controlador_jogo = ControladorJogo.ControladorJogo(sistema)
        controlador_usuario = ControladorUsuario.ControladorUsuario(sistema)
        controlador_transportadora = ControladorTransportadora.ControladorTransportadora(sistema)
        clientes = controlador_usuario.recuperarClientes()
        gerentes = controlador_usuario.recuperarGerentes()
        transportadoras = controlador_transportadora.recuperarTransportadoras()
        jogos = controlador_jogo.recuperarJogos()

        for jogo in jogos:
            aux_jogo.append(str(jogo.codigo) + "-" + jogo.nome)
        for cliente in clientes:
            aux_cliente.append(str(cliente.codigo) + "-" + cliente.nome)
        for gerente in gerentes:
            aux_gerente.append(str(gerente.codigo) + "-" + gerente.nome)
        for transportadora in transportadoras:
            aux_transportadora.append(str(transportadora.codigo) + "-" + transportadora.nome)



        cadastroVenda = \
            [
                [sg.Text('Código: ', font=('Verdana', 10, 'bold'), size=espaco),
                 sg.InputText(size=(20, 0), key='codigo')],
                [sg.Text('Cliente: ', font=('Verdana', 10, 'bold'), size=espaco),
                    sg.Combo(aux_cliente, default_value='Selecione um Cliente', key='comboCliente', size=(100, 0))],
                [sg.Text('Gerente: ', font=('Verdana', 10, 'bold'), size=espaco),
                    sg.Combo(aux_gerente, default_value='Selecione um Gerente', key='comboGerente', size=(100, 0))],
                [sg.Text('Data da Venda: ', font=('Verdana', 10, 'bold'), size=espaco),
                 sg.InputText(size=(20, 0), key='dataVenda')],
                [sg.Text('Itens Venda: ', font=('Verdana', 10, 'bold'), size=espaco)],
                [sg.Table(values=[], headings=['Código', 'Código Produto', 'Valor', 'Quantidade'],
                          key='tabelaItensVenda', enable_events=True, auto_size_columns=True,
                          display_row_numbers=True)],
                [sg.Text('Novo Item: ', font=('Verdana', 10, 'bold'), size=espaco),
                 sg.InputText(size=(10, 0), key='novoCodigo'),
                 sg.Combo(aux_jogo, default_value='Selecione um Produto', key='comboProduto', size=(10, 0)),
                 sg.InputText(size=(10, 0), key='novoQuantidade'),
                 sg.Button('Adicionar Item', key='adicionarItem')],
                [sg.Text('Possui Itens Físicos: ', font=('Verdana', 10, 'bold'), size=espaco),
                 sg.Radio('Sim', 'possuiItensFisicos', key='simPossui'),
                 sg.Radio('Não', 'possuiItensFisicos', key='naoPossui')],
                [sg.Text('Forma de Pagamento: ', font=('Verdana', 10, 'bold'), size=espaco),
                 sg.Radio('Boleto', 'formaPagamento', key='boleto'), sg.Radio('Cartão de Crédito', 'formaPagamento', key='cartaoCredito'), sg.Radio('PIX', 'formaPagamento', key='pix')],
                [sg.Text('Transportadora: ', font=('Verdana', 10, 'bold'), size=espaco),
                    sg.Combo(aux_transportadora, default_value='Selecione uma Transportadora', key='comboTransportadora', size=(100, 0))],
                [sg.Text('Não é possível fechar o programa durante o cadastro!', text_color='red')],
                [sg.Button('Salvar', key='salvarVenda', size=(15, 1)),
                 sg.Button('Cancelar', key='cancelar', size=(15, 1))]
            ]
        return sg.Window('Cadastro de Venda', cadastroVenda, finalize=True, size=frame_size,
                         relative_location=popup_location, element_justification='c', no_titlebar=True,
                         grab_anywhere=False, modal=True)
    elif type == 'boleto':
        boleto = \
            [
                [sg.Text('Pagamento Boleto', font=('Verdana', 10, 'bold'))],
                [sg.Text('Código: ', font=('Verdana', 10, 'bold'), size=espaco),
                sg.InputText(size=(20, 0), key='codigo')],
                [sg.Text('Número: ', font=('Verdana', 10, 'bold'), size=espaco),
                sg.InputText(size=(20, 0), key='numero')],
                [sg.Button('Salvar', key='salvar', size=(15, 1)),
                sg.Button('Cancelar', key='cancelar', size=(15, 1))]

            ]
        return sg.Window('Cadastro de Boleto', boleto, finalize=True, size=frame_size,
                         relative_location=popup_location, element_justification='c', no_titlebar=True,
                         grab_anywhere=False, modal=True)
    elif type == 'cartaoCredito':
        cartaoCredito = \
        [
            [sg.Text('Cadastrar/Pagamento Cartão de Crédito', font=('Verdana', 10, 'bold'))],
            [sg.Text('Código: ', font=('Verdana', 10, 'bold'), size=espaco),
            sg.InputText(size=(20, 0), key='codigo')],
            [sg.Text('Nome: ', font=('Verdana', 10, 'bold'), size=espaco),
            sg.InputText(size=(20, 0), key='nome')],
            [sg.Text('Bandeira: ', font=('Verdana', 10, 'bold'), size=espaco),
               sg.InputText(size=(20, 0), key='bandeira')],
            [sg.Text('Número: ', font=('Verdana', 10, 'bold'), size=espaco),
            sg.InputText(size=(20, 0), key='numero')],
            [sg.Button('Salvar', key='salvar', size=(15, 1)),
            sg.Button('Cancelar', key='cancelar', size=(15, 1))]
        ]
        return sg.Window('Cadastro de Cartão de Crédito', cartaoCredito, finalize=True, size=frame_size,
                            relative_location=popup_location, element_justification='c', no_titlebar=True,
                            grab_anywhere=False, modal=True)
    elif type == 'pix':
        pix = \
        [
            [sg.Text('Pagamento PIX', font=('Verdana', 10, 'bold'))],
            [sg.Text('Código: ', font=('Verdana', 10, 'bold'), size=espaco),
            sg.InputText(size=(20, 0), key='codigo')],
            [sg.Text('Chave: ', font=('Verdana', 10, 'bold'), size=espaco),
            sg.InputText(size=(20, 0), key='chave')],
            [sg.Button('Salvar', key='salvar', size=(15, 1)),
            sg.Button('Cancelar', key='cancelar', size=(15, 1))]
        ]
        return sg.Window('Cadastro de PIX', pix, finalize=True, size=frame_size,
                            relative_location=popup_location, element_justification='c', no_titlebar=True,
                            grab_anywhere=False, modal=True)

    elif type == 'relatorios':
        aux_desen = []
        aux_clien = []
        mes = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10','11','12']
        controlador_desenvolvedora = ControladorDesenvolvedora.ControladorDesenvolvedora(sistema)
        desenvolvedoras = controlador_desenvolvedora.recuperarDesenvolvedoras()
        for desenvolvedora in desenvolvedoras:
            aux_desen.append(str(desenvolvedora.codigo) + "-" + desenvolvedora.nome)

        controlador_usuario = ControladorUsuario.ControladorUsuario(sistema)
        clientes = controlador_usuario.recuperarClientes()
        for cliente in clientes:
            aux_clien .append(str(cliente.codigo) + "-" + cliente.nome)



        relatorios = \
            [
                [sg.Text('Selecione o relatório desejado:', font=('Verdana', 10, 'bold'), size=(30, 0))],
                [sg.Combo(['Listar todos os Jogos cadastrados.',
                           'Listar todos os Jogos da categoria Ação.',
                           'Listar todos os Jogos da categoria Aventura.',
                           'Listar todos os Jogos da categoria RPG.',
                           'Listar todos os Jogos da categoria Esporte.',
                           'Listar todos os Jogos da categoria Corrida.',
                           'Listar os dez Jogos mais caros',
                           'Listar os dez Jogos mais baratos',
                           'Listar todos os Jogos ordenados de forma crescente por nota de avaliação (A)',
                           'Listar todos os Jogos ordenados de forma crescente por nota de avaliação (B)',
                           'Listar todos as Desenvolvedoras cadastrados.',
                           'Listar as Desenvolvedoras que tiveram mais jogos vendidos.',
                           'Listar as Desenvolvedoras que tiveram o maior valor (lucro) de Jogos vendidos.',
                           'Listar todas as Transportadoras',
                           'Listar todos os Gerentes cadastrados.',
                           'Listar todos os Clientes cadastrados.',
                           'Listar todos os Clientes Épicos cadastrados.',
                           'Listar os dez Clientes com maior nível na plataforma.',
                           'Listar o histórico de Vendas de um Cliente em específico.',
                           'Listar todas as Vendas realizadas.',
                           'Listar Vendas realizadas em um mês em específico e o total de lucro gerado no mês.',
                           'Listar Vendas de uma Desenvolvedora especifica realizadas em um mês em específico e o total de lucro gerado no mês',
                           'Listar todas as Vendas pagas em Boleto.',
                           'Listar todas as Vendas pagas com Cartão de Crédito.',
                           'Listar todas as Vendas pagas com PIX.'],
                          default_value='Listar todos os Jogos cadastrados.', key='comboRelatorios', size=(100, 0))],
                [sg.Text('Desenvolvedora: ', font=('Verdana', 10, 'bold'), size=espaco),
                    sg.Combo(aux_desen, default_value='Selecione uma Desenvolvedora', key='comboDesenvolvedora', size=(100, 0))],
                [sg.Text('Mês: ', font=('Verdana', 10, 'bold'), size=espaco),
                    sg.Combo(mes, default_value='Selecione um Mês', key='comboMes', size=(100, 0))],
                [sg.Text('Cliente: ', font=('Verdana', 10, 'bold'), size=espaco),
                    sg.Combo(aux_clien , default_value='Selecione um Cliente', key='comboCliente', size=(100, 0))],
                [sg.Text('Não é possível fechar o programa durante o acesso aos relatórios!', text_color='red')],
                [sg.Button('Enviar', key='enviarRelatorio', size=(15, 1)),
                 sg.Button('Cancelar', key='cancelar', size=(15, 1))],
                [sg.Multiline(size=(100, 20), key='relatorio', disabled=True)]
            ]
        return sg.Window('Relatórios', relatorios, finalize=True, size=(700, 700),
                         element_justification='c')
    elif type == 'inicial':
        telaInicial = \
            [
                [sg.Text("Seja Bem-Vindo ao Ice Cube Games!", font=('Verdana', 20, 'bold'))],
                [sg.Text("Por favor, selecione uma das opções abaixo:", font=('Verdana', 10, 'bold'))],
                [sg.Button('Cadastrar Gerente', key='cadastrarGerente', size=(30, 2))],
                [sg.Button('Cadastrar Cliente', key='cadastrarCliente', size=(30, 2))],
                [sg.Button('Cadastrar Desenvolvedora', key='cadastrarDesenvolvedora', size=(30, 2))],
                [sg.Button('Cadastrar Transportadora', key='cadastrarTransportadora', size=(30, 2))],
                [sg.Button('Cadastrar Jogo', key='cadastrarJogo', size=(30, 2))],
                [sg.Button('Cadastrar Venda', key='cadastrarVenda', size=(30, 2))],
                [sg.Button('Relatórios', key='relatorios', size=(30, 2))],
            ]

        return sg.Window('Tela Inicial', telaInicial, finalize=True, size=(700, 500),
                         element_justification='c')
