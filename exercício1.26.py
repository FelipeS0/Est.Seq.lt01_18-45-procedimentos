#Declaração de Variáveis
n1: int = 0
n2: int = 0
aux: int = 0
#Início
n1 = int(input("qual o valor de N1?"))
n2 = int(input("qual o valor de N2?"))
def multíplo():
 if n1 > n2:
    aux = (n1 % n2 == 0)
    print ("N1 é múltiplo de N2")
 elif aux := (n2 % n1 == 0):
    print ("N2 é múltiplo de N1")
 elif aux := (n1 % n2 == 1):
    print (n1, "não é múltiplo de", n2)
 else: 
    aux = (n2 % n1 == 1)
    print (n2, "não é múltiplo de", n1)
multíplo()
#fim  