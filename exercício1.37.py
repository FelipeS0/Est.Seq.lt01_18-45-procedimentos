#Definição de Variáveis
n: int = 0
cont: int = 1
a: int = 0
b: int = 1
c: int = 0

#Início
n = int(input("Qual o número que deseja ver da sequência de fibonacci?"))
def sequência_fibonacci():
 for cont in range (1, n + 1, 1):
    a = b
    b= a + c
    c = a
    cont = cont + 1
    print (c)
sequência_fibonacci()
#fim