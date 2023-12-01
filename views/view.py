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

        if type == 'cadastrarGerente':
            cadastroGerente = \
                [
                    [sg.Column(layout=[
                        [sg.Text('Codigo: ', font=('Verdana', 10, 'bold'))],
                        [sg.Text('Nome: ', font=('Verdana', 10, 'bold'))],
                        [sg.Text('CPF', font=('Verdana', 10, 'bold'))],
                        [sg.Text('RG:', font=('Verdana', 10, 'bold'))],
                        [sg.Text('Data de Nascimento: ', font=('Verdana', 10, 'bold'))],
                        [sg.Text('Endereço: ', font=('Verdana', 10, 'bold'))],
                        [sg.Text('CEP: ', font=('Verdana', 10, 'bold'))],
                        [sg.Text('E-Mail: ', font=('Verdana', 10, 'bold'))],
                        [sg.Text('Salario: ', font=('Verdana', 10, 'bold'))],
                        [sg.Text('PIS: ', font=('Verdana', 10, 'bold'))],
                        [sg.Text('Data de Admissão: ', font=('Verdana', 10, 'bold'))]
                    ], element_justification='1'),
                        sg.Column(layout=[
                            [sg.InputText(size=(20, 1), key='codigo')],
                            [sg.InputText(size=(20, 1), key='nome')],
                            [sg.InputText(size=(20, 1), key='cpf')],
                            [sg.InputText(size=(20, 1), key='rg')],
                            [sg.InputText(size=(20, 1), key='dataNascimento')],
                            [sg.InputText(size=(20, 1), key='endereco')],
                            [sg.InputText(size=(20, 1), key='email')],
                            [sg.InputText(size=(20, 1), key='cep')],
                            [sg.InputText(size=(20, 1), key='salario')],
                            [sg.InputText(size=(20, 1), key='pis')],
                            [sg.InputText(size=(20, 1), key='dataAdmissao')]
                        ], element_justification='1')
                    ]
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
                    [sg.Column(layout=[
                        [sg.Text('Codigo: ', font=('Verdana', 10, 'bold'))],
                        [sg.Text('Nome: ', font=('Verdana', 10, 'bold'))],
                        [sg.Text('CPF', font=('Verdana', 10, 'bold'))],
                        [sg.Text('RG:', font=('Verdana', 10, 'bold'))],
                        [sg.Text('Data de Nascimento: ', font=('Verdana', 10, 'bold'))],
                        [sg.Text('Endereço: ', font=('Verdana', 10, 'bold'))],
                        [sg.Text('CEP: ', font=('Verdana', 10, 'bold'))],
                        [sg.Text('E-Mail: ', font=('Verdana', 10, 'bold'))],
                        [sg.Text('Data de Cadastro: ', font=('Verdana', 10, 'bold'))],
                        [sg.Text('Nível: ', font=('Verdana', 10, 'bold'))],
                        [sg.Text('É cliente épico? ', font=('Verdana', 10, 'bold'))]
                    ], element_justification='1'),
                        sg.Column(layout=[
                            [sg.InputText(size=(20, 1), key='codigo')],
                            [sg.InputText(size=(20, 1), key='nome')],
                            [sg.InputText(size=(20, 1), key='cpf')],
                            [sg.InputText(size=(20, 1), key='rg')],
                            [sg.InputText(size=(20, 1), key='dataNascimento')],
                            [sg.InputText(size=(20, 1), key='endereco')],
                            [sg.InputText(size=(20, 1), key='email')],
                            [sg.InputText(size=(20, 1), key='cep')],
                            [sg.InputText(size=(20, 1), key='dataCadastro')],
                            [sg.InputText(size=(20, 1), key='nivel')],
                            [sg.InputText(size=(20, 1), key='clienteEpico')]
                        ], element_justification='1')
                    ]
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
                    [sg.Column(layout=[
                        [sg.Text('Codigo: ', font=('Verdana', 10, 'bold'))],
                        [sg.Text('CNPJ: ', font=('Verdana', 10, 'bold'))],
                        [sg.Text('Nome:', font=('Verdana', 10, 'bold'))],
                        [sg.Text('E-Mail:', font=('Verdana', 10, 'bold'))],
                        [sg.Text('Site: ', font=('Verdana', 10, 'bold'))],
                        [sg.Text('Rede Social: ', font=('Verdana', 10, 'bold'))],
                        [sg.Text('Endereço: ', font=('Verdana', 10, 'bold'))]
                    ], element_justification='1'),
                        sg.Column(layout=[
                            [sg.InputText(size=(20, 1), key='codigo')],
                            [sg.InputText(size=(20, 1), key='cnpj')],
                            [sg.InputText(size=(20, 1), key='nome')],
                            [sg.InputText(size=(20, 1), key='email')],
                            [sg.InputText(size=(20, 1), key='site')],
                            [sg.InputText(size=(20, 1), key='redeSocial')],
                            [sg.InputText(size=(20, 1), key='endereco')]
                        ], element_justification='1')
                    ]
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
                    [sg.Column(layout=[
                        [sg.Text('Codigo: ', font=('Verdana', 10, 'bold'))],
                        [sg.Text('CNPJ: ', font=('Verdana', 10, 'bold'))],
                        [sg.Text('Nome:', font=('Verdana', 10, 'bold'))],
                        [sg.Text('E-Mail:', font=('Verdana', 10, 'bold'))],
                        [sg.Text('Telefone: ', font=('Verdana', 10, 'bold'))],
                        [sg.Text('Endereço: ', font=('Verdana', 10, 'bold'))],
                        [sg.Text('Tempo de Entrega: ', font=('Verdana', 10, 'bold'))]
                    ], element_justification='1'),
                        sg.Column(layout=[
                            [sg.InputText(size=(20, 1), key='codigo')],
                            [sg.InputText(size=(20, 1), key='cnpj')],
                            [sg.InputText(size=(20, 1), key='nome')],
                            [sg.InputText(size=(20, 1), key='email')],
                            [sg.InputText(size=(20, 1), key='telefone')],
                            [sg.InputText(size=(20, 1), key='endereco')],
                            [sg.InputText(size=(20, 1), key='tempoEntrega')]
                        ], element_justification='1')
                    ]
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
                    [sg.Column(layout=[
                        [sg.Text('Codigo: ', font=('Verdana', 10, 'bold'))],
                        [sg.Text('Nome: ', font=('Verdana', 10, 'bold'))],
                        [sg.Text('Tipo:', font=('Verdana', 10, 'bold'))],
                        [sg.Text('Desrição:', font=('Verdana', 10, 'bold'))],
                        [sg.Text('Desenvolvedora: ', font=('Verdana', 10, 'bold'))],
                        [sg.Text('Data de Lançamento: ', font=('Verdana', 10, 'bold'))],
                        [sg.Text('Valor: ', font=('Verdana', 10, 'bold'))],
                        [sg.Text('Requisitos Mínimos: ', font=('Verdana', 10, 'bold'))],
                        [sg.Text('Avaliação: ', font=('Verdana', 10, 'bold'))],
                        [sg.Text('Comentários: ', font=('Verdana', 10, 'bold'))],
                        [sg.Text('Disponível: ', font=('Verdana', 10, 'bold'))]
                    ], element_justification='1'),
                        sg.Column(layout=[
                            [sg.InputText(size=(20, 1), key='codigo')],
                            [sg.InputText(size=(20, 1), key='nome')],
                            [sg.InputText(size=(20, 1), key='tipo')],
                            [sg.InputText(size=(20, 1), key='descricao')],
                            [sg.InputText(size=(20, 1), key='desenvolvedora')],
                            [sg.InputText(size=(20, 1), key='dataLancamento')],
                            [sg.InputText(size=(20, 1), key='valor')],
                            [sg.InputText(size=(20, 1), key='requisitosMinimos')],
                            [sg.InputText(size=(20, 1), key='avaliacao')],
                            [sg.InputText(size=(20, 1), key='comentarios')],
                            [sg.InputText(size=(20, 1), key='disponivel')]
                        ], element_justification='1')
                    ]
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
                    [sg.Column(layout=[
                        [sg.Text('Codigo: ', font=('Verdana', 10, 'bold'))],
                        [sg.Text('Cliente: ', font=('Verdana', 10, 'bold'))],
                        [sg.Text('Gerente: ', font=('Verdana', 10, 'bold'))],
                        [sg.Text('Data de Venda: ', font=('Verdana', 10, 'bold'))],
                        [sg.Text('Itens Venda: ', font=('Verdana', 10, 'bold'))],
                        [sg.Text('Possui Itens Físicos: ', font=('Verdana', 10, 'bold'))],
                        [sg.Text('Valor Total: ', font=('Verdana', 10, 'bold'))],
                        [sg.Text('Valor com Descontos: ', font=('Verdana', 10, 'bold'))],
                        [sg.Text('Forma de Pagamento: ', font=('Verdana', 10, 'bold'))],
                        [sg.Text('Transportadora: ', font=('Verdana', 10, 'bold'))]
                    ], element_justification='1'),
                        sg.Column(layout=[
                            [sg.InputText(size=(20, 1), key='codigo')],
                            [sg.InputText(size=(20, 1), key='cliente')],
                            [sg.InputText(size=(20, 1), key='gerente')],
                            [sg.InputText(size=(20, 1), key='dataVenda')],
                            [sg.InputText(size=(20, 1), key='itensVenda')],
                            [sg.InputText(size=(20, 1), key='possuiItensFisicos')],
                            [sg.InputText(size=(20, 1), key='valorTotal')],
                            [sg.InputText(size=(20, 1), key='valorDesconto')],
                            [sg.InputText(size=(20, 1), key='formaDePagamento')],
                            [sg.InputText(size=(20, 1), key='transportadora')]
                        ], element_justification='1')
                    ]
                    [sg.Text('Não é possível fechar o programa durante o cadastro!', text_color='red')],
                    [sg.Button('Salvar', key='salvarVenda', size=(15, 1)),
                     sg.Button('Cancelar', key='cancelar', size=(15, 1))]
                ]
            return sg.Window('Cadastro de Venda', cadastroVenda, finalize=True, size=frame_size,
                             relative_location=popup_location, element_justification='c', no_titlebar=True,
                             grab_anywhere=False, modal=True)

