# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# – EQUILÁTERO: todos os lados iguais
# – ISÓSCELES: dois lados iguais, um diferente
# – ESCALENO: todos os lados diferentes

a = float(input("Digite um segmento do triangulo: "))
b = float(input("Digite o outro segmento do triangulo: "))
c = float(input("Digite o terceiro segmento do triangulo: "))
if a < (b + c) and b < (a + c) and c < (a +b):
    print("Com as medidas {}, {} e {} o triangulo é possível de ser formado!".format(a, b, c))
    if a == b and a == c:
        print("Além disso, o triangulo é EQUILÁTERO!")
    elif a == b and a != c:
        print("Além disso, o triangulo é ISÓCELES!")
    elif a != b and a != c and b != c:
        print("Além disso, o triangulo é ESCALENO")
else:
    print("Com as medidas {}, {} e {} o triangulo não é possível de ser formado!".format(a, b, c))
