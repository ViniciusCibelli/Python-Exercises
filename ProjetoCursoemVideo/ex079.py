# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

lista = []
while True:
    numero = lista.append(int(input("Digite um número: ")))

    resposta = str(input("Deseja continuar? [S/N] ")).strip().upper()
    while resposta != 'S' and resposta != 'N':
        print("Resposta INVÁLIDA, tente novamente!")
        resposta = str(input("Deseja continuar? [S/N] ")).strip().upper()
    if resposta == 'S':
        print("Certo! Adicione outro número: ")
    elif resposta == 'N':
        break

print(set(lista)) #põe em ordem e remove os duplicados
print(list(dict.fromkeys(lista))) #não põe em ordem e remove os duplicados

"""
numeros = list()
while True:
    n = int(input("Digite um número: "))
    if n not in numeros:
        numeros.append(n)
    else:
        print("Valor repitido... não vou adicionar!")

    resposta = str(input("Deseja continuar? [S/N] ")).strip().upper()
    while resposta != 'S' and resposta != 'N':
        print("Resposta INVÁLIDA, tente novamente!")
        resposta = str(input("Deseja continuar? [S/N] ")).strip().upper()
    if resposta == 'S':
        print("Certo! Adicione outro número: ")
    elif resposta == 'N':
        break
        
numeros.sort()
print(numeros)
"""