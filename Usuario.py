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

    def __str__(self):
        return f"Código do Usuário: {self._codigo}\n" \
               f"Nome: {self._nome}\n" \
               f"CPF: {self._cpf}\n" \ 
               f"RG: {self._rg}\n" \
               f"Data de Nascimento: {self._dataNascimento}\n" \
               f"Endereço: {self._endereco}\n" \
               f"CEP: {self._endereco}\n" \
               f"Email: {self._email}"

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


class Client(Usuario):
    def __init__(self, codigo, nome, cpf, rg, dataNascimento, endereco, cep, email, dataCadastro, nivel, clienteEpico):
        super().__init__(codigo, nome, cpf, rg, dataNascimento, endereco, cep, email)
        self._dataCadastro = dataCadastro
        self._nivel = nivel
        self._clienteEpico = clienteEpico

    def __str__(self):
        usuarioStr = super().__str__()
        return f"{usuarioStr}\n" \ 
               f"Data de Cadastro: {self._dataCadastro}\n" \
               f"Nivel: {self._nivel}\n" \
               f"Cliente Epico: {self._clienteEpico}"

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


class Gerente(Usuario):
    def __init__(self, codigo, nome, cpf, rg, dataNascimento, endereco, cep, email, salario, pis, dataAdmissao):
        super().__init__(codigo, nome, cpf, rg, dataNascimento, endereco, cep, email)
        self._salaio = salario
        self._pis = pis
        self._dataAdmissao = dataAdmissao

    def __str__(self):
        usuarioStr = super().__str__()
        return f"{usuarioStr}\n" \
               f"Salario: {self._salaio}\n" \
               f"PIS: {self._pis}\n" \
               f"Data de Admissão: {self._dataAdmissao}"

    @property
    def salario(self):
        return self._salaio

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



