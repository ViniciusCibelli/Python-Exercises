# Escreva um programa para aprovar o empréstimo bancário
# para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

valor = float(input("Qual o valor da casa desejada? R$"))
salario = float(input("Qual é o seu salário? R$"))
anos = int(input("Em quantos anos você pretende pagar o emprestimo? "))
if salario * 0.3 > valor / (anos * 12):
    print("Seu emprestimo foi \033[32mAPROVADO\033[m! \nEm {} anos você consiguirá pagar sua casa!".format(anos))
else:
    print("Infelizmente seu emprestimo foi \033[31mREPROVADO\033[m!")