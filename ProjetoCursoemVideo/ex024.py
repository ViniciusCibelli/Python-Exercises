"""Crie um programa que leia o nome de uma cidade e,
 diga se ela começa ou não com SANTO
"""

cidade = input("Digite o nome de uma cidade: ").strip().split()
print("O nome da cidade começa com 'Santo' ?")
print("SANTO" in cidade[0])
