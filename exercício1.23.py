#Declaração de Variáveis
n1: int = 0
n2: int = 0
n3: int = 0
n4: int = 0

#Início
n1 = int(input("Qual o primeiro valor?"))
n2 = int(input("Qual o segundo valor?"))
n3 = int(input("Qual o terceiro valor?"))
n4 = int(input("Qual o quarto valor?"))
def ordem_crescente():
 if n4<n1:
    print ("Sua escala crescente é:", n4, n1, n2, n3)
 elif n4<n2: 
    print ("Sua escala crescente é: ", n1, n4, n2, n3)
 elif n4<n3:
    print ("Sua escala crescente é:", n1, n2, n4, n3)
 else:
    print ("Sua escala crescente é:", n1, n2, n3, n4)
ordem_crescente()
#fim