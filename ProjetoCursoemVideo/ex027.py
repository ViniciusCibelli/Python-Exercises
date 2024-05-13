"""
Faça um programa que leia o nome completo de uma pessoa,
mostrando em seguida o primeiro e o ultimo nome separadamente. Ex:
Primeiro nome: Vinícius
Último nome: Negrini
"""

nome = str(input("Digite seu nome completo: ")).strip()
print("O seu primeiro nome é: {}!\nSeu último nome é: {}!".format(nome.split()[0], nome.rsplit()[-1]))
