class Desenvolvedora:

    def __init__(self, codigo, cnpj, nome, email, site, redeSocial, endereco):
        self.__codigo = codigo
        self.__cnpj = cnpj
        self.__nome = nome
        self.__email = email
        self.__site = site
        self.__redeSocial = redeSocial
        self.__endereco = endereco

    #Getter's e Setter'
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
    def site(self):
        return self.__site

    @site.setter
    def site(self, site):
        self.__site = site

    @property
    def redeSocial(self):
        return self.__redeSocial

    @redeSocial.setter
    def redeSocial(self, redeSocial):
        self.__redeSocial = redeSocial

    @property
    def endereco(self):
        return self.__endereco

    @endereco.setter
    def endereco(self, endereco):
        self.__endereco = endereco


    #StringToString
    def __str__(self):
        return f'\nCódigo: {self.__codigo}\nCNPJ: {self.__cnpj}\nNome: {self.__nome}\nEmail: {self.__email}\nSite: {self.__site}\nRede social: {self.__redeSocial}\nEndereço: {self.__endereco}\n'