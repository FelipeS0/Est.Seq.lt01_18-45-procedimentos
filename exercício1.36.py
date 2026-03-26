#Declaração de Variáveis
n: int = 0
cont: int = 0
aux: int = 1

#Início
n = int(input("Qual o número que deseja ver a fração fatorial?"))
def fração_fatorial():
 for cont in range(1, n + 1, 1):
    if cont ==1:
        print ("1 +",)
    
    aux*= cont
    print("1/", aux)
    cont = cont + 1
fração_fatorial()
#fim
    