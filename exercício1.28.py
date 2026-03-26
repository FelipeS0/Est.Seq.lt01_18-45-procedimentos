#Declaração de Variáveis
venda_M: int = 0
P_Atual: int = 0
p_Novo: float = 0.0

#Início
venda_M = int(input("Qual o  valor de vendas mensais do produto?"))
P_Atual = int(input("Qual o  valor do produto?"))
def venda_preço():
 if venda_M <500 and P_Atual <30:
    p_Novo = (P_Atual + (P_Atual * 0.10))
    print ("O novo valor do produto é:", p_Novo)
 elif venda_M >= 500 and venda_M < 1000 and P_Atual >= 30 and P_Atual <80:
    p_Novo = (P_Atual + (P_Atual * 0.15))
    print ("O novo valor do produto é:", p_Novo)
 elif  venda_M >= 1000 and P_Atual >= 80:
    p_Novo = (P_Atual - (P_Atual * 0.05))
    print ("O novo valor do produto é:", p_Novo)
 else:
    p_Novo = P_Atual
    print ("O novo valor do produto é:", p_Novo)
venda_preço()
#fim