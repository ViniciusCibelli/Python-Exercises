# Desenvolva um programa que leia quatro valores pelo teclado
# e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

numeros = (int(input("Digite o 1° número: ")),
           int(input("Digite o 2° número: ")),
           int(input("Digite o 3° número: ")),
           int(input("Digite o 4° número: ")))

print(f"O número '9' apareceu {numeros.count(9)} vezes!")
if 3 in numeros:
    print(f"O primeiro valor '3' apareceu na posição {numeros.index(3)+1} !")
else:
    print("O valor '3' não foi digitado!")
print(f"Os números pares são: ", end='')
for n in numeros:
    if n % 2 == 0:
        print(n, end=' ')
    else:
       print("...não foram digitados números pares!")
       break
