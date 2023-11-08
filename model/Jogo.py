from abc import ABC, abstractmethod
import datetime



class Jogo(ABC):

    def __init__(self, codigo, nome, descricao, desenvolvedora, dataLancamento, valor, requisitosMinimos, avaliacao, comentario, disponivel):
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

    @abstractmethod
    def calcularValor():
        pass

    def atualizarAvaliacao():
        pass
        
    def estaDisponivel():
        pass

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


    #Getter's e Setter's



class Acao(Jogo):
    def __init__(self, codigo, nome, descricao, desenvolvedora, dataLancamento, valor, requisitosMinimos, avaliacao, comentario, disponivel):
        super.__init__(codigo, nome, descricao, desenvolvedora, dataLancamento, valor, requisitosMinimos, avaliacao, comentario, disponivel)

    def calcularValor(self):
        return self.valor() * 0.0225

    #StringToString
    def __str__(self):
        pass 



class Aventura(Jogo):
    def __init__(self, codigo, nome, descricao, desenvolvedora, dataLancamento, valor, requisitosMinimos, avaliacao, comentario, disponivel):
        super.__init__(codigo, nome, descricao, desenvolvedora, dataLancamento, valor, requisitosMinimos, avaliacao, comentario, disponivel)

    def calcularValor(self):
        return self.valor() * 0.055

    #StringToString
    def __str__(self):
        pass 


class RPG(Jogo):
    def __init__(self, codigo, nome, descricao, desenvolvedora, dataLancamento, valor, requisitosMinimos, avaliacao, comentario, disponivel):
        super.__init__(codigo, nome, descricao, desenvolvedora, dataLancamento, valor, requisitosMinimos, avaliacao, comentario, disponivel)

    def calcularValor(self):
        return self.valor() * 0.0375

    #StringToString
    def __str__(self):
        pass 



class Esporte(Jogo):
    def __init__(self, codigo, nome, descricao, desenvolvedora, dataLancamento, valor, requisitosMinimos, avaliacao, comentario, disponivel):
        super.__init__(codigo, nome, descricao, desenvolvedora, dataLancamento, valor, requisitosMinimos, avaliacao, comentario, disponivel)

    def calcularValor(self):
        return self.valor() * 0.0075

    #StringToString
    def __str__(self):
        pass 



class Corrida(Jogo):
    def __init__(self, codigo, nome, descricao, desenvolvedora, dataLancamento, valor, requisitosMinimos, avaliacao, comentario, disponivel):
        super.__init__(codigo, nome, descricao, desenvolvedora, dataLancamento, valor, requisitosMinimos, avaliacao, comentario, disponivel)

    def calcularValor(self):
        return self.valor() * 0.0725

    #StringToString
    def __str__(self):
        pass 
