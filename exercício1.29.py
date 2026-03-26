#Declaração de Variáveis 
Pou1: int = 0
Ren2: int = 0
Aux: int = 0
Valor: float = 0.0
Valor_cor: float = 0.0

#Início
Valor = float(input("Qual o valor do investimento?"))
Aux =  int(input(" Qual o tipo de investimento? 1 = poupança e 2 = renda fixa"))
def investimento():
   if Aux == 1: 
    Valor_cor = (Valor + (Valor * 0.03 ))
    print ("Seu valor corrigido    será:", Valor_cor)
   elif Aux == 2:
    Valor_cor = (Valor + float(Valor * 0.05))
    print ("Seu valor corrigido    será:", Valor_cor)
   else:
    print ("Não foi possível determinar o investimento desejado, tente novamente")
investimento()
#fim