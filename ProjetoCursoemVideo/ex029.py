#Escreva um programa que leia a velocidade de um carro.
#Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar R$7,00 por cada Km acima do limite.

from time import sleep
velocidade = float(input("Diga qual a velocidade atual do carro: "))
sleep(1)
multa = (velocidade - 80)*7
if velocidade <= 80:
    print("Tudo bem, você não foi multado!")
else:
    print("Putz! Aparentemente, você foi multado.")
    sleep(1)
    print("O valor da multa é R$7,00 por Km acima do limite.")
    sleep(1)
    print("Você terá que pagar {} reais pela multa".format(multa))
    sleep(1)
    print("Da próxima vez, mantenha-se dentro dos limites de velocidade!")
print("-=-"*20)
