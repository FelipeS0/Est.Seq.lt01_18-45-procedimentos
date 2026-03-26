#Declaração de Variáveis
n: int = 1
n2: int = 0
cont: int = 1

#Início
def fatorial_fração():
 for cont in range (1, 15, 1):
    if cont ==1:
        print ("1 - ", end="")
    n = n + 1
    n2 = n * n    
    cont = cont + 1
    if cont !=15:
     print (n, "/" ,n2 , end=" + ")
    else:
     print (n, " / ", n2, end="  ")
fatorial_fração()
#fim