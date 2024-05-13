# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
# já na posição correta de inserção sem usar o sort(). No final, mostre a lista ordenada na tela.

numeros = list()
for c in range(0, 5):
    n = int(input("Digite um número: "))

    if c == 0 or n > numeros[-1]:
        numeros.append(n)
        print("Adicionando ao final da lista...")

    else:
        posicao = 0
        while posicao < len(numeros):
            if n <= numeros[posicao]:
                numeros.insert(posicao, n)
                print(f"Adicionando na posição {posicao} da lista...")
                break
            posicao += 1
print("Os valores adicionados a lista foram: ", end='')
print(numeros)
