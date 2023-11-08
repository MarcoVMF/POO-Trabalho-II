class Transportadora:
    def __init__(self, codigo, cnpj, nome, email, telefone, endereco, tempoEntrega):
        self.__codigo = codigo
        self.__cnpj = cnpj
        self.__nome = nome
        self.__email = email
        self.__telefone = telefone
        self.__endereco = endereco
        self.__tempoEntrega = tempoEntrega


    #Getter's e Setter's
    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    @property
    def cnpj(self):
        return self.__cnpj

    @cnpj.setter
    def cnpj(self, cnpj):
        self.__cnpj = cnpj

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone

    @property
    def endereco(self):
        return self.__endereco

    @endereco.setter
    def endereco(self, endereco):
        self.__endereco = endereco

    @property
    def tempoEntrega(self):
        return self.__tempoEntrega

    @tempoEntrega.setter
    def tempoEntrega(self, tempoEntrega):
        self.__tempoEntrega = tempoEntrega

    #StringToString
    def __str__(self):
        return f"Código: {self.codigo} \nCNPJ: {self.cnpj} \nNome: {self.nome} \nEmail: {self.email} \nTelefone: {self.telefone} \nEndereço: {self.endereco} \nTempo de Entrega: {self.tempoEntrega}"
    