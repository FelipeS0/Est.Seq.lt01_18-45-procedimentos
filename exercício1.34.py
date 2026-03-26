#Declaração de Variáveis
N: int = 0
cont: int = 1
aux: int = 1

#Início
N = int(input("Qual número você deseja ver a tabuada?"))
def tabuada():
 while cont <11:
  aux = N * cont
  cont = cont + 1
  print (aux)
tabuada()
 #fim