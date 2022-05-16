from br.ufsc.exemplo.amigo import Amigo
from br.ufsc.exemplo.genero import Genero
from br.ufsc.exemplo.livro import Livro

class Sistema:

    def __init__(self):
        self.__livros = []
        self.__generos = []
        self.__amigos = []
        self.__emprestimos = []

    def mostra_menu_opcoes(self):

        while True:
            print("**** SISTEMA LIVROS ****")
            print("1 - Cadastra Amigo")
            print("2 - Cadastra Livro")
            print("3 - Cadastra Genero")
            print("4 - Cadastra Emprestimo")
            print("5 - Lista Amigos")
            print("0 - Finaliza")
            opcao_escolhida = input("Opcao: ")

            if opcao_escolhida == "1":
                self.cadastra_amigo()
            elif opcao_escolhida == "2":
                self.cadastra_livro()
            elif opcao_escolhida == "3":
                self.cadastra_genero()
            elif opcao_escolhida == "4":
                self.cadastra_genero()
            elif opcao_escolhida == "5":
                self.lista_amigos()
            elif opcao_escolhida == "0":
                break


    def cadastra_amigo(self):
        print("**** CADASTRA AMIGO ****")
        nome = input("Nome: ")
        telefone = input("Telefone: ")

        amigo = Amigo(telefone, nome)

        self.__amigos.append(amigo)

    def cadastra_genero(self):
        print("**** CADASTRA GENERO ****")
        codigo = input("Codigo do Genero: ")
        nome = input("Nome do Genero: ")

        genero = Genero(codigo, nome)

        self.__generos.append(genero)


    def lista_amigos(self):
        print("**** LISTA DOS AMIGOS ****")
        for amigo in self.__amigos:
            print(f"Nome: {amigo.nome}")
            print(f"Telefone: {amigo.telefone}")

    def lista_generos(self):
        print("**** LISTA DOS GENEROS ****")
        for genero in self.__generos:
            print(f"{genero.codigo} - {genero.nome}")

    def busca_genero(self, codigo):
        for genero in self.__generos:
            if genero.codigo == codigo:
                return genero


    def cadastra_livro(self):
        titulo = input("Titulo: ")
        autor = input("Autor: ")


        print("Selecione o Genero: ")
        self.lista_generos()
        codigo_genero = input("Codigo do Genero")
        genero = self.busca_genero(codigo_genero)

        livro = Livro(titulo, genero)



sistema = Sistema()
sistema.mostra_menu_opcoes()