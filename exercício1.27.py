#Declaração de Variáveis
vol: int = 0
ext_circuito: int = 0
ext_circuito_km: int = 0
tempo: int = 0
tempoH:int = 0
vel_M: float = 0.0

#Início
vol = int(input("Qual o total de voltas dadas?"))
ext_circuito = int(input("Qual o total do tamanho do circuito?"))
tempo = int(input("Qual o total de tempo?"))
def velocidade_média():
 ext_circuito_km = ext_circuito / 1000
 tempoH = tempo /60
 vel_M = float(ext_circuito_km / tempoH)
 print ("A velocidade média é:", vel_M)
velocidade_média()
#fim
