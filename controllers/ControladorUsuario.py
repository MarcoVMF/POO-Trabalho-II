from models import Usuario, BancoDeDados, SistemaJogosEletronicos
class ControladorUsuario:
    def __init__(self, sistema):
        self.__bancodedados = BancoDeDados.BancoDeDados()
        self.__sistema = sistema

    #CLIENTE
    def criarCliente(self, codigo, nome, cpf, rg, dataNascimento, endereco, cep, email, dataCadastro, nivel, clienteEpico, pagamento):
        cliente = Usuario.Cliente(codigo, nome, cpf, rg, dataNascimento, endereco, cep, email, dataCadastro, nivel, clienteEpico, pagamento)
        return cliente

    def inserirCliente(self, cliente):
        self.__bancodedados.inserirCliente(cliente)
        self.__sistema.atualizarDados()

    def recuperarCliente(self, codigo):
        return self.__bancodedados.recuperarCliente(codigo)

    def recuperarClientes(self):
        return self.__bancodedados.recuperarClientes()

    def removerCliente(self, codigo):
        self.__bancodedados.removerCliente(codigo)
        self.__sistema.atualizarDados()


    #GERENTE
    def criarGerente(self, codigo, nome, cpf, rg, dataNascimento, endereco, cep, email, salario, pis, dataAdmissao):
        gerente = Usuario.Gerente(codigo, nome, cpf, rg, dataNascimento, endereco, cep, email, salario, pis, dataAdmissao)
        return gerente

    def inserirGerente(self, gerente):
        self.__bancodedados.inserirGerente(gerente)
        self.__sistema.atualizarDados()

    def recuperarGerente(self, codigo):
        return self.__bancodedados.recuperarGerente(codigo)

    def recuperarGerentes(self):
        return self.__bancodedados.recuperarGerentes()

    def removerGerente(self, codigo):
        self.__bancodedados.removerGerente(codigo)
        self.__sistema.atualizarDados()
