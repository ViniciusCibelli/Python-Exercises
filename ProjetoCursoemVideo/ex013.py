# Faça um algoritimo que leia o salário de um funcionario e mostre seu novo valor com um aumento de 15%

s = float(input("Digite o valor do seu salário "))
a = int(input("Digite a porcentagem de aumento desejada "))
ns = (s/100)*a + s
print('-'*30)
print("Com um aumento de \033[32m{0}%\033[m, o salário passará a ser: \033[33m{1}\033[m reais".format(a, ns))
