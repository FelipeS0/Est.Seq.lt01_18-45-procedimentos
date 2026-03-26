#Declaração de Variáveis
N1: int = 0
N2: int = 0
cont: int = 0
aux: int = 0
aux2: int = 0

#Início
N1 = int(input("Qual o primeiro número?"))
N2 = int(input("Qual o segundo número?"))
def números_primos():
 if N2>N1:
    aux2 = N2
    N2 = N1
    N1 = aux2
 for cont in range (N2, N1, 1):
    if cont % 2 ==1:
        aux+= cont
 print (aux)
números_primos()
#fim