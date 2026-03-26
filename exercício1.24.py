#Declaração de Variáveis
n1:  int = 0

#Início
n1 = int(input("Qual o valor do número?"))
def divisão_2_3():
 if (n1 % 2 == 0) and (n1 % 3 == 0):
    print ("Seu número é divisível por 2 e 3")
 elif  (n1 % 2 ==0) and (n1 % 3 ==1):
    print ("Seu número é divisível por 2, mas não por 3")
 else:
    print ("Seu número não é divisível por 2 e 3")
divisão_2_3()    
#fim
    