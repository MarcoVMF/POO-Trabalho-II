from abc import ABC, abstractmethod

class Usuario(ABC):
    def __init__(self, codigo, nome, cpf, rg, dataNascimento, endereco, cep, email):
        self._codigo = codigo
        self._nome = nome
        self._cpf = cpf
        self._rg = rg
        self._dataNascimento = dataNascimento
        self._endereco = endereco
        self._cep = cep
        self._email = email

    @property
    def codigo(self):
        return self._codigo

    @property
    def nome(self):
        return self._nome

    @property
    def cpf(self):
        return self._cpf

    @property
    def rg(self):
        return self._rg

    @property
    def dataNascimento(self):
        return self._dataNascimento

    @property
    def endereco(self):
        return self._endereco

    @property
    def cep(self):
        return self._cep

    @property
    def email(self):
        return self._email

    @codigo.setter
    def codigo(self, codigo):
        self._codigo = codigo

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @cpf.setter
    def cpf(self, cpf):
        self._cpf = cpf

    @rg.setter
    def rg(self, rg):
        self._rg = rg

    @dataNascimento.setter
    def dataNascimento(self, dataNascimento):
        self._dataNascimento = dataNascimento

    @endereco.setter
    def endereco(self, endereco):
        self._endereco = endereco

    @cep.setter
    def cep(self, cep):
        self._cep = cep

    @email.setter
    def email(self, email):
        self._email = email

    #StringToString
    def __str__(self):
        return (f"\n======Usuário======"
                f"\nCódigo: {self.codigo}"
                f"\nNome: {self.nome}"
                f"\nCPF: {self.cpf}"
                f"\nRG: {self.rg}"
                f"\nData de Nascimento: {self.dataNascimento}"
                f"\nEndereço: {self.endereco}"
                f"\nCEP: {self.cep}"
                f"\nEmail: {self.email}"
                f"\n===================\n")

class Cliente(Usuario):
    def __init__(self, codigo, nome, cpf, rg, dataNascimento, endereco, cep, email, dataCadastro, nivel, clienteEpico, pagamento):
        super().__init__(codigo, nome, cpf, rg, dataNascimento, endereco, cep, email)
        self._dataCadastro = dataCadastro
        self._nivel = nivel
        self._clienteEpico = clienteEpico
        self._pagamento = pagamento


    @property
    def dataCadastro(self):
        return self._dataCadastro

    @property
    def nivel(self):
        return self._nivel

    @property
    def clienteEpico(self):
        return self._clienteEpico

    @dataCadastro.setter
    def dataCadastro(self, dataCadastro):
        self._dataCadastro = dataCadastro

    @nivel.setter
    def nivel(self, nivel):
        self._nivel = nivel

    @clienteEpico.setter
    def clienteEpico(self, clienteEpico):
        self._clienteEpico = clienteEpico

    @property
    def pagamento(self):
        return self._pagamento

    @pagamento.setter
    def pagamento(self, pagamento):
        self._pagamento = pagamento

    #StringToString
    def __str__(self):
        return (f"\n======Cliente======"
                f"\nCódigo: {super().codigo}"
                f"\nNome: {super().nome}"
                f"\nCPF: {super().cpf}"
                f"\nRG: {super().rg}"
                f"\nData de Nascimento: {super().dataNascimento}"
                f"\nEndereço: {super().endereco}"
                f"\nCEP: {super().cep}"
                f"\nEmail: {super().email}"
                f"\nData de Cadastro: {self.dataCadastro}"
                f"\nNível: {self.nivel}"
                f"\nCliente Épico: {self.clienteEpico}"
                f"\nPagamento: {self.pagamento}"
                f"\n===================\n")

class Gerente(Usuario):
    def __init__(self, codigo, nome, cpf, rg, dataNascimento, endereco, cep, email, salario, pis, dataAdmissao):
        super().__init__(codigo, nome, cpf, rg, dataNascimento, endereco, cep, email)
        self._salario = salario
        self._pis = pis
        self._dataAdmissao = dataAdmissao

    @property
    def salario(self):
        return self._salario

    @property
    def pis(self):
        return self._pis

    @property
    def dataAdmissao(self):
        return self._dataAdmissao

    @salario.setter
    def salario(self, salario):
        self._salario = salario

    @pis.setter
    def pis(self, pis):
        self._pis = pis

    @dataAdmissao.setter
    def dataAdmissao(self, dataAdmissao):
        self._dataAdmissao = dataAdmissao

    #StringToString
    def __str__(self):
        return (f"\n======Gerente======"
                f"\nCódigo: {super().codigo}"
                f"\nNome: {super().nome}"
                f"\nCPF: {super().cpf}"
                f"\nRG: {super().rg}"
                f"\nData de Nascimento: {super().dataNascimento}"
                f"\nEndereço: {super().endereco}"
                f"\nCEP: {super().cep}"
                f"\nEmail: {super().email}"
                f"\nData de Cadastro: {self.salario}"
                f"\nNível: {self.pis}"
                f"\nCliente Épico: {self.dataAdmissao}"
                f"\n===================\n")