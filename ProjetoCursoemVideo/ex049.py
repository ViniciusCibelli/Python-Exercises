# Refaça o DESAFIO 9,
# mostrando a tabuada de um número que o usuário escolher,
# só que agora utilizando um laço for.

n = int(input("Diga um número que você deseja saber a tabuada: "))
for c in range(0, 11):
    print("{} x {:2} = {}".format(n, c, (c * n)))
print("FIM")