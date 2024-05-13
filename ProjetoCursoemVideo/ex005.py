# Faça um programa que leia um número inteiro e mostre na seu sucessor e seu anterior

ni = int(input("Digite um número "))
a = ni-1
s = ni+1
print("="*30)
print("O número foi: \033[33m{0:.1f}\033[m, seu anterior é: \033[31m{1:.1f}\033[m e seu sucessor é: \033[32m{2:.1f}\033[m".format(ni, ni-1, ni+1))
# print("O número foi: {0:.1f}, seu anterior é: {1:.1f} e seu sucessor é: {2:.1f}".format(ni, a, s))
