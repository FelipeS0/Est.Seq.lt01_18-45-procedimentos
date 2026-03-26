#Declaração de variáveis
HHi: int = 0
MMi: int = 0
HHf: int = 0
MMf: int = 0
aux: int = 0
aux2: int = 0
RM: int = 0
HT: int = 0
MF: int = 0
#Início
HHi = int(input("Que horas começou?"))
MMi = int(input("Que minutos começou?"))
HHf = int(input("Que horas terminou?"))
MMf = int(input("Que minutos terminou?"))
aux = (HHi * 60) + MMi
aux2 = (HHf * 60) + MMf
def horário_passado():
 if aux > aux2:
    HT = int(((aux2 + 1440) - aux) /60)
    MF = (((aux2 + 1440) - aux) % 60)
    print ("O tempo total é:", HT, "horas e", MF, "minutos.")
 else:
    HT = int(((aux2 - aux) /60))
    MF = ((aux2 - aux) % 60)
    print ("O tempo total é:", HT, "horas e", MF, "minutos.")
horário_passado()
#fim