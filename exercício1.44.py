#Declaração de Variáveis
base: int = 0
expoente: int = 0
result: int = 0

#Início
base = int(input("Qual a base da exponenciação?"))
expoente = int(input("Qual o expoente para potenciar a base?"))
def resultado_exponenciação():
 result = base ** expoente
 print (result)
resultado_exponenciação
#fim