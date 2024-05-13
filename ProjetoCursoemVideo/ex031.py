#Desenvolva um programa que pergunte a distância de uma viagem em Km.
#Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e
#R$0,45 parta viagens mais longas.

from time import sleep
distancia = float(input("Qual a distância, em Km, da viagem que você irá fazer? "))
if distancia <= 200:
    sleep(1)
    p1 = distancia*0.5
    print("A passagem de uma viagem de {} Km custará {} reais!".format(distancia, p1))
else:
    sleep(1)
    p2 = distancia*0.45
    print("A passagem de uma viagem de {} Km custará {} reais!".format(distancia, p2))
sleep(1)
print("Boa Viagem!")
