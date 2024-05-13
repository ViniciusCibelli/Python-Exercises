# Escreva um programa que leia dois números inteiros e compare-os.
# Mostrando na tela uma mensagem:

# - O primeiro valor é maior

# - O segundo valor é maior

# - Não existe valor maior, os dois são iguais
numero1 = float(input("Digite um número: "))
numero2 = float(input("Digite outro número: "))
if numero1 > numero2:
    print("O \033[33mprimeiro número\033[m é maior que o \033[31msegundo número\033[m!")
elif numero1 == numero2:
    print("O \033[33mprimeiro número\033[m e o \033[31msegundo número\033[m são iguais")
else:
    print("O \033[31msegundo número\033[m é maior que o \033[33mprimeiro número\033[m!")