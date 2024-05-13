# Desenvolva um programa que leia as duas notas de um aluno, calcula e mostra a média

p1 = float(input("Nota da P1: "))
p2 = float(input("Nota da P2: "))
s = p1 + p2 # ou (p1 + p2)/2
m = s/2
print('='*20)
print("A soma das notas desse aluno é: \033[33m{0}\033[m \nE sua média é: \033[34m{1}\033[m".format(s, m))
if m >= 6:
    print("\033[32mVocê foi aprovado!\033[m")
else:
    print("\033[31mVocê foi reprovado, estude mais!\033[m")