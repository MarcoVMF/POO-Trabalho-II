from models import BancoDeDados, SistemaJogosEletronicos
import PySimpleGUI as sg

def telaInicial():
    espaco = (20, 0)
    sistema = SistemaJogosEletronicos.SistemaJogosEletronicos()
    if sistema == None or sistema == '':
        layout_TelaInicial = \
            [
                [sg.Text('Nome da Plataforma: ', font=('Verdana', 10, 'bold'), size=espaco),
                     sg.InputText(size=(20, 0), key='nome')],
                [sg.Button('Salvar', key='salvar')]
            ]
        window = sg.Window('Primeiro Uso', layout_TelaInicial, finalize=True, no_titlebar=True,
                           grab_anywhere=False, modal=True)

        event, values = window.read()
        while True:
            if event == sg.WINDOW_CLOSED:
                window.close()
                break
            if event == 'salvar':
                if values['nome'] != '':
                    sistema.__nomePlataforma = values['nome']
                    return values['nome']
                    break
                else:
                    popup = sg.popup_error('Todos os campos devem ser preenchidos!')

    else:
        return sistema['__nomePlataforma']