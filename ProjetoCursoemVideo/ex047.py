# Crie um programa que mostre na tela todos os
# números pares que estão no intervalo entre 1 e 50.

print("Todos os números pares entre 1 e 50 são:")
for c in range(1, 51):
    if (c % 2) == 0:
        print(c, end=' ')
print("Fim!")