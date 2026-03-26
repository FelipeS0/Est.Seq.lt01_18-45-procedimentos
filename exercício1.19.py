#Declaração de Variáveis
n1: int = 0
n2: int = 0
aux: int = 0

#início
n1 = int(input("Qual o seu número 1?"))
n2 = int(input("Qual o seu número 2?"))
def maior_e_menor():
    global n1
    global n2
    global aux
    if (n2>n1):
     aux = n2
     n2 = n1
     n1 = aux
    print (n1, "É maior que", n2)

maior_e_menor() 
#fim