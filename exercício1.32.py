#Declaração de Variáveis
N: int = 0
cont: int = 0
aux: int = 1

#Início
N = int(input("Qual o  número que deseja ver o fatorial?"))
def  fatorial():
 for cont in range (N, 1, -1):
    aux*= N 
    N = N-1
    print (aux)
fatorial()
#fim