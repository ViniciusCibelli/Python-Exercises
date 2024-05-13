"""
Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e,
a quantidade de dias pelos quais ele foi alugado.
Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
"""
kp = float(input("Quantos km foram percorridos pelo carro? "))
da = float(input("Quantos dias esse mesmo carro foi alugado? "))
ppk = kp * 0.15
ppd = da * 60
pt = ppk + ppd
print("-"*45)
print("O valor cobrado pelos dias alugados é: \033[33m{}\033[m".format(ppd))
print("O valor a ser cobrado pelos km é: \033[31m{}\033[m".format(ppk))
print("O valor total a pagar é: \033[32m{0:.2f}\033[m".format(pt))
