# Escreva um programa que pergunte o salário de um funcionário e calcule o valor
# do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input("Qual é o valor do seu salário? "))
if salario > 1250.00:
    salarion = (salario * 0.1) + salario
    print("Com um aumento de 10%, o seu novo salário será: R${0:.2f}".format(salarion))
else:
    salarion = (salario * 0.15) + salario
    print("Com um aumento de 15%, o seu novo salário será: R${0:.2f}".format(salarion))
"""
if salario <= 1250.00:
    salarion = (salario * 0.15) + salario
    print("Com um aumento de 15%, o seu novo salário será: R${0:.2f}".format(salarion))
"""