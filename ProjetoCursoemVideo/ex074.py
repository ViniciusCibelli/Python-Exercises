# Crie um programa que vai gerar cinco números aleatórios e
# colocar em uma tupla. Depois disso, mostre a listagem de números gerados
# e também indique o menor e o maior valor que estão na tupla.

menor = maior = 0
from random import randint
numeros = (randint(0, 10), randint(0, 10), randint(0, 10),
           randint(0, 10), randint(0, 10))
print(f"Eu sorteei os valores: {numeros}")
print(f"O maior valor sorteado foi: {max(numeros)}")
print(f"O menor valor sorteado foi: {min(numeros)}")
