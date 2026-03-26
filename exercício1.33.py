#Declaração de Variáveis
N: int = 0
cont: int = 0
aux: int = 1

#Início
N = int(input("Qual o número da sequência?"))
def sequência_fração():
 for cont in range (1, N + 1, 1):
    if cont == 1:
        print ("1 +", end="")
        
    print (" 1/", cont , end=" + ")
    cont = cont + 1   
sequência_fração() 
#fim