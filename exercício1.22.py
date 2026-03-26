#Declaração de Variáveis
n1: int = 0
n2: int = 0
aux: int = 0
#Início
n1 = int(input("Qual o seu primeiro número"))
n2 = int(input("Qual o seu segundo número"))
def sequência_crescente():
 if n2>n1:
    aux = n2
    n2 = n1
    n1 = n2
    print ("Sua sequência crescente é:", n1, "e", aux)

 else:
    print ("Sua sequência crescente é:", n2, "e", n1)
sequência_crescente()
#fim