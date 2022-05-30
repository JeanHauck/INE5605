

# Definindo as Classes
class Pessoa:
    def __init__(self, cpf: int, nome: str):
        self.__cpf = cpf
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf: str):
        self.__cpf = cpf

    def validado(self):
        if (self.__cpf is not None) and (self.__nome is not None):
            print("PESSOA VALIDADA")

# Cliente herda de Pessoa
class Cliente(Pessoa):
    def __init__(self, codigo: int, cpf: int, nome: str):
        super().__init__(cpf, nome)
        self.__codigo = codigo
        print("NOME DA PESSOA:", self.nome)

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo: int):
        self.__codigo = codigo

    def validado(self):
        print("INVOCANDO O METODO VALIDADO DO CLIENTE")
        super().validado()
        if (self.__codigo is not None):
            print("CLIENTE VALIDADO!")


class ClienteEspecial(Cliente):
    def __init__(self, desconto: int, codigo: int, cpf: int, nome: str):
        super().__init__(codigo, cpf, nome)
        self.__desconto = desconto


# Exercitando os conceitos


cliente = Cliente(1, 12345, "Jean")
pessoa = Pessoa(45678, "Outro Nome")

cliente.validado()
