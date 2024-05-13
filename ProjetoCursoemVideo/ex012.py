# Faça um algoritimo que leia um número e mostre seu novo preço com 5% de desconto

v = float(input("Digite algum valor "))
nv = v - (v/100)*5
print('-'*20)
print("\033[33m{}\033[m com 5% de desconto é: \033[32m{}\033[m".format(v, nv))
