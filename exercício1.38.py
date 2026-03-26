#Declaração de Variáveis
n: float = 0.0
aux: float = 0.0
cont: int = 1
m: float = 0.1
o: float = 0.0

#Início
def Sequência_reais_100():
 while cont < 101:
   n = float(input("Qual o número real selecionado"))
   if cont == 1:
      aux = n
   elif n > aux:
      aux = n
   elif n < m:
       m = n
   cont = cont + 1     
 print ("seu menor número é:", m , "é o maior é:", aux)
Sequência_reais_100()
#fim