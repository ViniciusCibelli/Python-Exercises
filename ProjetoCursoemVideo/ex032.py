#Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

ano = int(input("Diga um ano qualquer: "))
anob = ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0
if anob:
    print("{} é um ano bissexto!".format(ano))
else:
    print("{} NÃO é um ano bissexto!".format(ano))
print('-=-'*10)
