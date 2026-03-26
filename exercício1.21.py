#Declaração de  Variáveis
n1: int = 0
n2: int = 0
n3: int = 0
n4: int = 0
média: float = 0.0

#Início
n1 = int(input("Qual a sua primeira nota?"))
n2 = int(input("Qual a sua segunda nota?"))
n3 = int(input("Qual a sua terceira nota?"))
n4 = int(input("Qual a sua quarta nota?"))
média = (n1 + n2 + n3 + n4) /4

def representação_média():
 if média >= 6.0:
    print ("Aprovado")
 elif média >= 3.0 < 6.0:
    print ("Exame")
 else:
    print ("Retido")
representação_média()
#fim
 
