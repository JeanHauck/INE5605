from controle.ctrl_usuario import CtrlUsuario
from visao.tela_sistema import TelaSistema

class CtrlSistema:
    def __init__(self):
        self.__ctrl_usuario = CtrlUsuario()
        self.__tela_sistema = TelaSistema()

    def iniciar(self):
        while True:
            opcao_escolhida = self.__tela_sistema.mostrar_menu_inicial()

            if opcao_escolhida == 1:
                if (self.__ctrl_usuario.logar()):
                    self.__ctrl_usuario.abre_tela_inicial()
            elif opcao_escolhida == 2:
                pass
            else:
                break

if __name__ == "__main__":
    CtrlSistema().iniciar()
