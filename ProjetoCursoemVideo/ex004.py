# Um programa que leia algo pelo teclado e mostre na tela o seu
# tipo primitivo e todas as informações possíveis sobre ela

algo = input("Digite qualquer coisa: ").strip()
print("O tipo primitivo desse valor é: {}".format(type(algo)))
print("É Número e Letra?", algo.isalnum())
print("É apenas número?", algo.isnumeric())
print("É apenas letra?", algo.isalpha())
print("São letras maiúsulas?", algo.isupper())
print("Possui a primeira letra em maiusculo?", algo.istitle())
print("São letras minusculas?", algo.islower())
print("É imprimivel?", algo.isprintable())
print("São apenas espaços?", algo.isspace())
