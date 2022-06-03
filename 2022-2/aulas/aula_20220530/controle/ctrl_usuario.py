from visao.tela_usuario import TelaUsuario
from entidade.usuario import Usuario

class CtrlUsuario:
    def __init__(self):
        self.__usuarios = [Usuario("admin", "admin")]
        self.__tela_usuario = TelaUsuario()
        self.__manter_tela = True

    def incluir(self):
        print("INCLUIR")

    def alterar(self):
        print("ALTERAR")

    def excluir(self):
        print("EXCLUIR")

    def listar(self):
        print("LISTAR")

    def retornar(self):
        self.__manter_tela = False

    def logar(self):
        # Pega dados do usuario
        dados_usuario = self.__tela_usuario.mostra_tela_login()

        # Procura por nome e senha
        for usuario in self.__usuarios:
            if (usuario.nome == dados_usuario["nome"]) and \
                 (usuario.senha == dados_usuario["senha"]):
                self.__tela_usuario.mostra_mensagem("Logado com Sucesso!")
                return usuario
        else:
            self.__tela_usuario.mostra_mensagem("Nome ou Senha invalidos!")
            return None

    def abre_tela_inicial(self):

        switcher = {0: self.retornar, 1: self.incluir, 2: self.alterar, 3: self.excluir, 4: self.listar}
        self.__manter_tela = True
        while self.__manter_tela:
            opcao_escolhida = self.__tela_usuario.mostra_tela_opcoes()
            funcao_escolhida = switcher[opcao_escolhida]
            funcao_escolhida()


