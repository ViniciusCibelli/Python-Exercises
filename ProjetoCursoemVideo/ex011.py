# Faça um programa que leia a altura e a largura de uma parede em metros,
# calcule sua area e a quantidade de tinta necessaria para pinta-la
# sabendo que 1L de tinta pinta 2m quadrados

a = float(input("Diga a altura da parede "))
l = float(input("Diga a largura da parede "))
A = a*l
from math import ceil
t = ceil(A/2)
print("A parede tem altura de \033[31m{}m\033[m e largura de \033[32m{}m\033[m, logo, a área é de \033[33m{}m²\033[m".format(a, l, A))
print("E, será necessário \033[34m{}\033[m latas de tinta".format(t))
