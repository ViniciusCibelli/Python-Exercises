"""
Faça um programa que leia uma frase e diga:
- Quantas vezes aparece a letra 'A'
- Em que posição 'A' aparece pela primeira vez
- Em que posição 'A' aparece pela última vez
"""

frase = str(input("Digite uma frase: ")).strip().upper()
print("Na frase acima, a letra 'A' aparece {} vezes!".format(frase.count('A')))
print("'A' aparece pela primeira vez na posição {}!".format(frase.find('A')))
print("'A' aparece pela última vez na posição {}!".format(frase.rfind('A')))

