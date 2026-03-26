#Declaração de Variáveis
n1: int = 1
n2: int = 6
cont: int = 0
#Início
def dados():
 for cont in range (1, n2 + 1, 1):
    if n1 + n2 == 7:
        print (n1, "+", n2, "=", 7)
    n1 = n1 + 1
    n2 = n2 - 1
dados()
#fim
