import PySimpleGUI as sg
import os
from models import SistemaJogosEletronicos
from datetime import datetime

'''sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.


# Create the Window
window = sg.Window('Window Title', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    print('You entered ', values[0])

window.close()'''

class tela:
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    caminho_icone = os.path.join(diretorio_atual, 'assets', 'tela_icon.ico')
    sg.theme('DarkAmber')

    def __init__(self, sistema):
        self.sistema = sistema

    @staticmethod
    def createWindow(type):
        #window = sg.Window('Window Title', layout)
        #frame_element = sg.Window.find_element(key='lugarAparacerCadastro')
        #frame_size = frame_element.Widget.winfo_reqwidth() - 15, frame_element.Widget.winfo_reqheight() - 15
        popup_location = (125, 0)
        espaco=(20,0)

        if type == 'cadastrarGerente':
            cadastroGerente = \
                [
                    [sg.Text('Código: ', font=('Verdana', 10, 'bold'), size=espaco),
                     sg.InputText(size=(20,0), key='codigo')],
                    [sg.Text('Nome: ', font=('Verdana', 10, 'bold'), size=espaco),
                     sg.InputText(size=(20,0), key='nome')],
                    [sg.Text('CPF: ', font=('Verdana', 10, 'bold'), size=espaco),
                     sg.InputText(size=(20,0), key='cpf')],
                    [sg.Text('RG: ', font=('Verdana', 10, 'bold'), size=espaco),
                     sg.InputText(size=(20,0), key='rg')],
                    [sg.Text('Data de Nascimento: ', font=('Verdana', 10, 'bold'), size=espaco),
                     sg.InputText(size=(20,0), key='dataNascimento')],
                    [sg.Text('Endereço: ', font=('Verdana', 10, 'bold'), size=espaco),
                     sg.InputText(size=(20,0), key='endereco')],
                    [sg.Text('CEP: ', font=('Verdana', 10, 'bold'), size=espaco),
                     sg.InputText(size=(20,0), key='cep')],
                    [sg.Text('E-Mail: ', font=('Verdana', 10, 'bold'), size=espaco),
                     sg.InputText(size=(20,0), key='email')],
                    [sg.Text('Salário: ', font=('Verdana', 10, 'bold'), size=espaco),
                     sg.InputText(size=(20,0), key='salario')],
                    [sg.Text('PIS: ', font=('Verdana', 10, 'bold'), size=espaco),
                     sg.InputText(size=(20,0), key='pis')],
                    [sg.Text('Data de Admissão: ', font=('Verdana', 10, 'bold'), size=espaco),
                     sg.InputText(size=(20,0), key='dataAdmissao')],
                    [sg.Text('Não é possível fechar o programa durante o cadastro!', text_color='red')],
                    [sg.Button('Salvar', key='salvarGerente', size=(15, 1)),
                     sg.Button('Cancelar', key='cancelar', size=(15, 1))]
                ]
            return sg.Window('Cadastro de Gerente', cadastroGerente, finalize=True, size=frame_size,
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
                     sg.Radio('Sim','clienteEpico',key='simEpico'),sg.Radio('Não','clienteEpico',key='naoEpico')],
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
            cadastroJogo = \
                [
                    [sg.Text('Código: ', font=('Verdana', 10, 'bold'), size=espaco),
                     sg.InputText(size=(20, 0), key='codigo')],
                    [sg.Text('Nome: ', font=('Verdana', 10, 'bold'), size=espaco),
                     sg.InputText(size=(20, 0), key='nome')],
                    [sg.Text('Tipo: ', font=('Verdana', 10, 'bold'), size=espaco),
                     sg.Radio('Ação','tipo',key='acao'),sg.Radio('Aventura','tipo',key='aventura'),sg.Radio('RPG','tipo',key='rpg'),sg.Radio('Esporte','tipo',key='esporte'),sg.Radio('Corrida','tipo',key='corrida')],
                    [sg.Text('Descrição: ', font=('Verdana', 10, 'bold'), size=espaco),
                     sg.InputText(size=(20, 0), key='descricao')],
                    [sg.Text('Desenvolvedora: ', font=('Verdana', 10, 'bold'), size=espaco),
                     sg.InputText(size=(20, 0), key='desenvolvedora')],
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
                     sg.Radio('Sim','disponivel',key='simDisponivel'),sg.Radio('Não','disponivel',key='naoDisponivel')],
                    [sg.Text('Não é possível fechar o programa durante o cadastro!', text_color='red')],
                    [sg.Button('Salvar', key='salvarJogo', size=(15, 1)),
                     sg.Button('Cancelar', key='cancelar', size=(15, 1))]
                ]
            return sg.Window('Cadastro de Jogo', cadastroJogo, finalize=True, size=frame_size,
                             relative_location=popup_location, element_justification='c', no_titlebar=True,
                             grab_anywhere=False, modal=True)

        elif type == 'cadastrarVenda':
            cadastroVenda = \
                [
                    [sg.Text('Código: ', font=('Verdana', 10, 'bold'), size=espaco),
                     sg.InputText(size=(20, 0), key='codigo')],
                    [sg.Text('Cliente: ', font=('Verdana', 10, 'bold'), size=espaco),
                     sg.InputText(size=(20, 0), key='cliente')],
                    [sg.Text('Gerente: ', font=('Verdana', 10, 'bold'), size=espaco),
                     sg.InputText(size=(20, 0), key='gerente')],
                    [sg.Text('Data da Venda: ', font=('Verdana', 10, 'bold'), size=espaco),
                     sg.InputText(size=(20, 0), key='dataVenda')],
                    [sg.Text('Itens Venda: ', font=('Verdana', 10, 'bold'), size=espaco),
                     sg.InputText(size=(20, 0), key='itensVenda')],
                    [sg.Text('Possui Itens Físicos: ', font=('Verdana', 10, 'bold'), size=espaco),
                     sg.Radio('Sim','possuiItensFisicos',key='simPossui'),sg.Radio('Não','possuiItensFisicos',key='naoPossui')],
                    [sg.Text('Valor Total: ', font=('Verdana', 10, 'bold'), size=espaco),
                     sg.InputText(size=(20, 0), key='valorTotal')],
                    [sg.Text('Valor com Descontos: ', font=('Verdana', 10, 'bold'), size=espaco),
                     sg.InputText(size=(20, 0), key='valorDesconto')],
                    [sg.Text('Forma de Pagamento: ', font=('Verdana', 10, 'bold'), size=espaco),
                     sg.InputText(size=(20, 0), key='formaPagamento')],
                    [sg.Text('Transportadora: ', font=('Verdana', 10, 'bold'), size=espaco),
                     sg.InputText(size=(20, 0), key='transportadora')],
                    [sg.Text('Não é possível fechar o programa durante o cadastro!', text_color='red')],
                    [sg.Button('Salvar', key='salvarVenda', size=(15, 1)),
                     sg.Button('Cancelar', key='cancelar', size=(15, 1))]
                ]
            return sg.Window('Cadastro de Venda', cadastroVenda, finalize=True, size=frame_size,
                             relative_location=popup_location, element_justification='c', no_titlebar=True,
                             grab_anywhere=False, modal=True)

        elif type == 'Relatórios':
            relatorios = \
                [
                    [sg.Text('Selecione o relatório desejado:', font=('Verdana', 10, 'bold'), size=(30,0))],
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
                              default_value='Listar todos os Jogos cadastrados.', key='comboRelatorios')],
                    [sg.Text('Não é possível fechar o programa durante o acesso aos relatórios!', text_color='red')],
                    [sg.Button('Avançar', key='avancarRelatorios', size=(15, 1)),
                     sg.Button('Cancelar', key='cancelar', size=(15, 1))]
                ]
            return sg.Window('Relatórios', relatorios, finalize=True, size=(150,80),
                             element_justification='c')