class Configuracao:
    def __init__(self, arquivoVendas, arquivoJogos, arquivoDesenvolvedoras, arquivoTransportadoras, arquivoClientes, arquivoGerentes):
        self.__arquivoVendas = arquivoVendas
        self.__arquivoJogos = arquivoJogos
        self.__arquivoDesenvolvedoras = arquivoDesenvolvedoras
        self.__arquivoTransportadoras = arquivoTransportadoras
        self.__arquivoClientes = arquivoClientes
        self.__arquivoGerentes = arquivoGerentes

    @property
    def arquivoVendas(self):
        return self.__arquivoVendas

    @arquivoVendas.setter
    def arquivoVendas(self, arquivoVendas):
        self.__arquivoVendas = arquivoVendas

    @property
    def arquivoJogos(self):
        return self.__arquivoJogos

    @arquivoJogos.setter
    def arquivoJogos(self, arquivoJogos):
        self.__arquivoJogos = arquivoJogos

    @property
    def arquivoDesenvolvedoras(self):
        return self.__arquivoDesenvolvedoras

    @arquivoDesenvolvedoras.setter
    def arquivoDesenvolvedoras(self, arquivoDesenvolvedoras):
        self.__arquivoDesenvolvedoras = arquivoDesenvolvedoras

    @property
    def arquivoTransportadoras(self):
        return self.__arquivoTransportadoras

    @arquivoTransportadoras.setter
    def arquivoTransportadoras(self, arquivoTransportadoras):
        self.__arquivoTransportadoras = arquivoTransportadoras

    @property
    def arquivoClientes(self):
        return self.__arquivoClientes

    @arquivoClientes.setter
    def arquivoClientes(self, arquivoClientes):
        self.__arquivoClientes = arquivoClientes

    @property
    def arquivoGerentes(self):
        return self.__arquivoGerentes

    @arquivoGerentes.setter
    def arquivoGerentes(self, arquivoGerentes):
        self.__arquivoGerentes = arquivoGerentes

