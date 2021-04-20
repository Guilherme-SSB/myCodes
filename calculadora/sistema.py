from os import system
from time import sleep


class Sistema(object):

    def executar(self):
        self._executarSistema = True
        while(self._executarSistema):
            Sistema.exibirMenu(self)
            opcao = int(input())
            Sistema.avaliarOpcao(self, opcao)

   
    def exibirMenu(self):
        Sistema.clearScreen(self)
        print("*======================================================*")
        print("|                                                      |")
        print("|             Bem-vindo à Calculadora v1.0             |")
        print("|           Desevolvido por Guilherme Samuel           |")
        print("|                                                      |")
        print("*======================================================*")
        print("|                    MENU DE OPÇÕES                    |")
        print("*======================================================*")
        print("|  0 - Sair da Calculadora                             |")
        print("|  1 - Trabalhar com números                           |")
        print("|  2 - Trabalhar com polinômios                        |")
        print("|  3 - Estatísca                                       |")
        print("|  4 - Conhecer o desenvolvedor                        |")
        print("*======================================================*")
        print()
        print("Informe sua opção: ")

    def avaliarOpcao(self, opcao):
        if opcao == 0:
            print("valeu falou")
            exit()

    def clearScreen(self):
        system("cls")
