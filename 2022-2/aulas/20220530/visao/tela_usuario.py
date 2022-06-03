

class TelaUsuario:
    def __init__(self):
        pass

    def mostra_tela_login(self):
        print("===== LOGIN =====")
        nome = input("Nome: ")
        senha = input("Senha: ")

        return {"nome": nome, "senha": senha}

    def mostra_mensagem(self, mensagem: str):
        print(mensagem)
        input("Clique <ENTER> para continuar")


    def mostra_tela_opcoes(self):
        print("======== CADASTRO USUARIOS ========")
        print("1 - Incluir Usuario")
        print("2 - Alterar Usuario")
        print("3 - Excluir Usuario")
        print("4 - Listar Usuario")
        print("0 - Retornar")
        opcao = int(input("Opcao: "))
        return opcao
