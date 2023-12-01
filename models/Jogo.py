from abc import ABC, abstractmethod
from datetime import datetime


class Jogo(ABC):

    def __init__(self, codigo, nome, descricao, desenvolvedora, dataLancamento, valor, requisitosMinimos, avaliacao, comentario, disponivel, tipo):
        self._codigo = codigo
        self._nome = nome
        self._descricao = descricao
        self._desenvolvedora = desenvolvedora
        self._dataLancamento = datetime.strptime(dataLancamento, "%d/%m/%Y")
        self._valor = valor
        self._requisitosMinimos = requisitosMinimos
        self._avaliacao = avaliacao
        self._comentario = comentario
        self._disponivel = disponivel
        self._tipo = tipo

    @abstractmethod
    def calcularValor(self):
        pass

    def atualizarAvaliacao(self, avaliacaoNova):
        self._avaliacao = (self._avaliacao + avaliacaoNova)/2
        return self._avaliacao
        
    def estaDisponivel(self):
        return self._disponivel

    #Getter's e Setter's

    @property
    def codigo(self):
        return self._codigo

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, tipo):
        self._tipo = tipo

    @codigo.setter
    def codigo(self, codigo):
        self._codigo = codigo

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def descricao(self):
        return self._descricao

    @descricao.setter
    def descricao(self, descricao):
        self._descricao = descricao

    @property
    def desenvolvedora(self):
        return self._desenvolvedora

    @desenvolvedora.setter
    def desenvolvedora(self, desenvolvedora):
        self._desenvolvedora = desenvolvedora

    @property
    def dataLancamento(self):
        return self._dataLancamento

    @dataLancamento.setter
    def dataLancamento(self, dataLancamento):
        self._dataLancamento = dataLancamento

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, valor):
        self._valor = valor

    @property
    def requisitosMinimos(self):
        return self._requisitosMinimos

    @requisitosMinimos.setter
    def requisitosMinimos(self, requisitosMinimos):
        self._requisitosMinimos = requisitosMinimos

    @property
    def avaliacao(self):
        return self._avaliacao

    @avaliacao.setter
    def avaliacao(self, avaliacao):
        self._avaliacao = avaliacao

    @property
    def comentario(self):
        return self._comentario

    @comentario.setter
    def comentario(self, comentario):
        self._comentario = comentario

    @property
    def disponivel(self):
        return self._disponivel

    @disponivel.setter
    def disponivel(self, disponivel):
        self._disponivel = disponivel

    #StringToString
    def __str__(self):
        return f"Código: {self._codigo} \nNome: {self._nome} \nDescrição: {self._descricao} \nDesenvolvedora: {self._desenvolvedora.__str__()} \nData de Lançamento: {self._dataLancamento} \nValor: {self._valor} \nRequisitos Mínimos: {self._requisitosMinimos} \nAvaliação: {self._avaliacao} \nComentário: {self._comentario} \nDisponível: {self._disponivel}"

class Acao(Jogo):

    def __init__(self, codigo, nome, descricao, desenvolvedora, dataLancamento, valor, requisitosMinimos, avaliacao, comentario, disponivel, tipo):
        super().__init__(codigo, nome, descricao, desenvolvedora, dataLancamento, valor, requisitosMinimos, avaliacao, comentario, disponivel, tipo)

    def calcularValor(self):
        return 0.0225 * super().valor

    #StringToString
    def __str__(self):
        return f"Código: {self._codigo} \nNome: {self._nome} \nDescrição: {self._descricao} \nDesenvolvedora: {str(self.desenvolvedora)} \n \nData de Lançamento: {self._dataLancamento} \nValor: {self.calcularValor()} \nRequisitos Mínimos: {self._requisitosMinimos} \nAvaliação: {self._avaliacao} \nComentário: {self._comentario} \nDisponível: {self._disponivel}"



class Aventura(Jogo):
    def __init__(self, codigo, nome, descricao, desenvolvedora, dataLancamento, valor, requisitosMinimos, avaliacao, comentario, disponivel, tipo):
        super().__init__(codigo, nome, descricao, desenvolvedora, dataLancamento, valor, requisitosMinimos, avaliacao, comentario, disponivel, tipo)

    def calcularValor(self):
        return super().valor * 0.055

    #StringToString
    def __str__(self):
        return f"Código: {self._codigo} \nNome: {self._nome} \nDescrição: {self._descricao} \nDesenvolvedora: {self._desenvolvedora.__str__()} \nData de Lançamento: {self._dataLancamento} \nValor: {self.calcularValor()} \nRequisitos Mínimos: {self._requisitosMinimos} \nAvaliação: {self._avaliacao} \nComentário: {self._comentario} \nDisponível: {self._disponivel}"

class RPG(Jogo):

    def __init__(self, codigo, nome, descricao, desenvolvedora, dataLancamento, valor, requisitosMinimos, avaliacao, comentario, disponivel, tipo):
        super().__init__(codigo, nome, descricao, desenvolvedora, dataLancamento, valor, requisitosMinimos, avaliacao, comentario, disponivel, tipo)

    def calcularValor(self):
        return super().valor * 0.0375

    #StringToString
    def __str__(self):
        return f"Código: {self._codigo} \nNome: {self._nome} \nDescrição: {self._descricao} \nDesenvolvedora: {self._desenvolvedora.__str__()} \nData de Lançamento: {self._dataLancamento} \nValor: {self.calcularValor()} \nRequisitos Mínimos: {self._requisitosMinimos} \nAvaliação: {self._avaliacao} \nComentário: {self._comentario} \nDisponível: {self._disponivel}"

class Esporte(Jogo):
    def __init__(self, codigo, nome, descricao, desenvolvedora, dataLancamento, valor, requisitosMinimos, avaliacao, comentario, disponivel, tipo):
        super().__init__(codigo, nome, descricao, desenvolvedora, dataLancamento, valor, requisitosMinimos, avaliacao, comentario, disponivel, tipo)

    def calcularValor(self):
        return super().valor * 0.0075

    #StringToString
    def __str__(self):
        return f"Código: {self._codigo} \nNome: {self._nome} \nDescrição: {self._descricao} \nDesenvolvedora: {self._desenvolvedora.__str__()} \nData de Lançamento: {self._dataLancamento} \nValor: {self.calcularValor()} \nRequisitos Mínimos: {self._requisitosMinimos} \nAvaliação: {self._avaliacao} \nComentário: {self._comentario} \nDisponível: {self._disponivel}"

class Corrida(Jogo):
    def __init__(self, codigo, nome, descricao, desenvolvedora, dataLancamento, valor, requisitosMinimos, avaliacao, comentario, disponivel, tipo):
        super().__init__(codigo, nome, descricao, desenvolvedora, dataLancamento, valor, requisitosMinimos, avaliacao, comentario, disponivel, tipo)

    def calcularValor(self):
        return super().valor * 0.0725

    #StringToString
    def __str__(self):
        return f"Código: {self._codigo} \nNome: {self._nome} \nDescrição: {self._descricao} \nDesenvolvedora: {self._desenvolvedora.__str__()} \nData de Lançamento: {self._dataLancamento} \nValor: {self.calcularValor()} \nRequisitos Mínimos: {self._requisitosMinimos} \nAvaliação: {self._avaliacao} \nComentário: {self._comentario} \nDisponível: {self._disponivel}"