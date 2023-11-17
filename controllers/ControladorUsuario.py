from models import Usuario, BancoDeDados, SistemaJogosEletronicos
class ControladorUsuario:
    def __init__(self):
        pass

    #CLIENTE
    def criarCliente(self, codigo, nome, cpf, rg, dataNascimento, endereco, cep, email, dataCadastro, nivel, clienteEpico):
        cliente = Usuario.Cliente(codigo, nome, cpf, rg, dataNascimento, endereco, cep, email, dataCadastro, nivel, clienteEpico)

    def inserirCliente(self, cliente):
        BancoDeDados.BancoDeDados.inserirCliente(cliente)
        SistemaJogosEletronicos.SistemaJogosEletronicos.atualizarDados()

    def recuperarCliente(self, codigo):
        return BancoDeDados.BancoDeDados.recuperarCliente(codigo)

    def removerCliente(self, codigo):
        BancoDeDados.BancoDeDados.removerCliente(codigo)
        SistemaJogosEletronicos.SistemaJogosEletronicos.atualizarDados()


    #GERENTE
    def criarGerente(self, codigo, nome, cpf, rg, dataNascimento, endereco, cep, email, salario, pis, dataAdmissao):
        gerente = Usuario.Gerente(codigo, nome, cpf, rg, dataNascimento, endereco, cep, email, salario, pis, dataAdmissao)

    def inserirGerente(self, gerente):
        BancoDeDados.BancoDeDados.inserirGerente(gerente)
        SistemaJogosEletronicos.SistemaJogosEletronicos.atualizarDados()

    def recuperarGerente(self, codigo):
        return BancoDeDados.BancoDeDados.recuperarGerente(codigo)

    def removerGerente(self, codigo):
        BancoDeDados.BancoDeDados.removerGerente(codigo)
        SistemaJogosEletronicos.SistemaJogosEletronicos.atualizarDados()
