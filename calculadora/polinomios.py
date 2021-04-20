class Polinomios(object):  

    def executarPolinomios(self):
        Polinomios.exibirMenuPolinomios(self)

    def exibirMenuPolinomios(self):
        print("*--------------------------------------------*")
        print("|        >TRABALHANDO COM POLINÔMIOS<        |")
        print("*============================================*")
        print("|  0 - Para achar as raízes                  |")
        print("|  1 - Para derivar o polinômio              |")
        print("|  2 - Para achar a integral do polinômio    |")
        print("|  3 - Para fazer todos os de cima           |")
        print("*============================================*")
        print()
        print("Informe sua opção: ")
        x = int(input())
