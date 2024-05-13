# Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

palavras = ('Banana', 'Morango', 'Pera', 'Melancia',
            'Minecraft', 'Dota', 'Terraria', 'Deceit',
            'Vinicin', 'Vinisao', 'Pepeuzete', 'Delux', 'Alberto')
for i in palavras:  # cada palavra em 'palavras' vira um indice 'i'
    print(f"\nAs vogais da palavra \033[34m{i.upper()}\033[m sâo: ", end='')
    for letra in i:  # para cada letra na palavra 'i' verifica se há as vogais
        if letra.lower() in "aeiou":  # se possui as vogais, as escreva
            print(letra, end=' ')
