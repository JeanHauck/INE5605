

class Amigo:
    def __init__(self, telefone, nome):
        self.__telefone = telefone
        self.__nome = nome

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone\

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome
