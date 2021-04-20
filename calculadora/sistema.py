from ast import Num
from os import system
from time import sleep
import numeros

classeDosNumeros = numeros.Numeros()
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
        print("|             Bem-vindo à Calculadora v2.0             |")
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
            sleep(0.5)
            Sistema.clearScreen(self)
            print("Obrigado por usar o programa")
            exit()

        elif opcao == 1:
            Sistema.clearScreen(self)
            print("Você escolheu trabalhar com números!\n")
            while (opcao == 1):
                classeDosNumeros.executarNumeros()


        elif opcao == 2:
            Sistema.clearScreen(self)
            print("Você escolheu trabalhar com polinômios!\n")
            # Chamar a classe polinomios

        elif opcao == 3:
            print("Essa função ainda não foi incrementada no programa. Aguarde por futuras atualizações\n")
            sleep(3)
            Sistema.executar(self)

        elif opcao == 4:
            pass
            # Chamar classe dev

        else:
            print("Escolha uma opção válida!\n")
            sleep(3)
            Sistema.executar(self)

    def clearScreen(self):
        system("cls")
