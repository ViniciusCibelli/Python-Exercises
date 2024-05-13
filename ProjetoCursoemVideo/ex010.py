# Crie um programa que mostre quantos dinheiros uma pessoa tem na carteira e mostre quantos dolares ela consegue comprar
# Cada real vale 3,27 dolares

vc = float(input("Quanto dinheiro você tem na carteira? "))
dc = vc/3.27
print('-'*30)
print("Com \033[33m{0}\033[m reais, você consegue comprar \033[32m{1:.1f}\033[m doláres".format(vc, dc))

#vc = float(input("Quanto dinheiro você tem na cartira? "))
#d = vc/3.27
#if vc < 3.27:
#    print("Com {0} reais você não consegue comprar nem um dólar".format(vc))
#else:
#    print("Com {0} reais você consegue comprar {1:.2} dolares".format(vc, d))