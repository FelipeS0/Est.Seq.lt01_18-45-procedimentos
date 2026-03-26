#Declaração de Variáveis
n1: int = 0
n2: int = 0
aux: int = 0 
dif: int = 0
#início
n1 = int(input("Qual o valor do primeiro número?"))
n2 = int(input("Qual o valor do segundo número?"))
if n2>n1:
 aux= n2
 n2= n1
 n1= aux
def Calcular_diferença():
 global dif
 global aux
 global n1
 global n2
 dif = (n1 - n2)
 print ("A diferença de valor entre", n1, "e", n2, "é:", dif)
 
Calcular_diferença() 
#fim