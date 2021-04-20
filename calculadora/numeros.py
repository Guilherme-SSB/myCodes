class Numeros(object):  

    def executarNumeros(self):
        Numeros.exibirMenuNumeros(self)

    def exibirMenuNumeros(self):
        print("*---------------------------------------*")
        print("|       >TRABALHANDO COM NÚMEROS<       |")
        print("*=======================================*")
        print("|  1 - Para somar                       |")
        print("|  2 - Para subtrair                    |")
        print("|  3 - Para dividir                     |")
        print("|  4 - Para multiplicar                 |")
        print("*=======================================*")
        print()
        print("Informe sua opção: ")
        x = int(input())
