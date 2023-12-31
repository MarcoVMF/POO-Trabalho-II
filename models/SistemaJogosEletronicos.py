from models import BancoDeDados

class SistemaJogosEletronicos:
    def __init__(self):
        self.__nomePlataforma = "Ice Cube"
        self.atualizarDados()

    def atualizarDados(self):
        self.__bancoDeDados = BancoDeDados.BancoDeDados()
        self.__vendas = self.__bancoDeDados.recuperarVendas()
        self.__jogos = self.__bancoDeDados.recuperarJogos()
        self.__desenvolvedora = self.__bancoDeDados.recuperarDesenvolvedoras()
        self.__transportadoras = self.__bancoDeDados.recuperarTransportadoras()
        self.__clientes = self.__bancoDeDados.recuperarClientes()
        self.__gerentes = self.__bancoDeDados.recuperarGerentes()
        self.__configuracoes = None
