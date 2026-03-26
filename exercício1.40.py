#Declaração de Variáveis
n1: int = 0
n2: int = 0
cont: int = 0
aux: int = 0
#Início
n1 = int(input("Qual o primeiro número?"))
n2 = int(input("Qual o segundo número?"))
def números_primos():
 if n2>n1:
   aux = n2
   n2 = n1
   n1 = aux
 for cont in range (1, n1, 1):
    if n2 % 2 ==1:
        aux = n2
        print (aux)
    n2 = n2 + 1    
    cont = cont + 1
números_primos()
#fim
    