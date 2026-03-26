#Declaração de Variáveis
n: int = 1
n2: int = 1
cont: int = 1

#Início
def sequência_1_2():
 for cont in range (1, 51, 1):
    if cont ==1:
        print ("1 + ", end=" ")
    if cont !=50:
        print (n,"/",n2, " + ", end= " ")
    if cont ==50:
        print (n,"/",n2, end= " ")
    n = n + 1
    n2+= 2
sequência_1_2()
#fim