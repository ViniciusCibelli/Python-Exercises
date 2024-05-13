# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
# desconsiderando os espaços. Exemplos de palíndromos:
# A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO

frase = input("Digite uma frase: ").split()
novafrase = ''.join(frase).upper()
i = 0
eh_palindromo = True

for c in range(len(novafrase)-1, -1, -1):
    print(novafrase[c], end='')
    if novafrase[c] != novafrase[i]:
        eh_palindromo = False
        break
    i += 1

if eh_palindromo:
    print("\nÉ palindromo")
else:
    print("\nNão é palindromo!")
#print("É palindromo" if eh_palindromo else "Não é palindromo")