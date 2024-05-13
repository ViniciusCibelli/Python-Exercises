# Desenvolva um programa que leia o comprimento de três retas e,
# diga ao usuário se elas podem ou não formar um triângulo.

a = float(input("Digite o valor do primeiro segmento: "))
b = float(input("Digite o valor do segundo segmento: "))
c = float(input("Digite o valor do terceiro segmento: "))
if a < (b + c) and b < (a + c) and c < (a + b):
    print("O triangulo de segmentos {}, {} e {} é possível de ser formado!".format(a, b, c))
else:
    print("O triangulo de segmentos {}, {} e {} NÃO é possível de ser formado!".format(a, b, c))
