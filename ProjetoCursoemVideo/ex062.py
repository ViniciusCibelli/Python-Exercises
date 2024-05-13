# Melhore o DESAFIO 61,
# perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.

print("{} GERADOR DE PAs {}".format('-=' * 5, '-=' * 5))
a1 = int(input("Digite o primeiro termo da sua PA: "))
razao = int(input("Digite a razão da sua PA: "))
cont = 0
pergunta = 'S'
quantidade = 10
while pergunta == 'S':
    while cont != quantidade:
        cont += 1
        na = a1 + (cont - 1) * razao
        print("O {:2}° termo da sua PA é: {}".format(cont, na))
    pergunta = str(input("Deseja saber mais termos? [S/N] ")).strip().upper()
    if pergunta == 'S':
        quantidade_a_mais = int(input("Quantos termos a mais? "))
        quantidade += quantidade_a_mais
    else:
        print("Tudo bem! Tenha um bom dia!")
print("FIM!")

"""
from time import sleep
print("{} GERADOR DE PAs {}".format('-=' * 5, '-=' * 5))
sleep(1)
a1 = int(input("Digite o primeiro termo da sua PA: "))
razao = int(input("Digite a razão da sua PA: "))
cont = 0
while cont != 10:
    cont += 1
    na = a1 + (cont - 1) * razao
    print("O {:2}° termo da sua PA é: {}".format(cont, na))
pergunta = str(input("Deseja saber mais termos? [S/N] ")).strip().upper()
if pergunta == 'S':
    quantidade = int(input("Quantos termos a mais? "))
    sleep(1)
    cont = 10
    while cont != (quantidade + 10):
        cont += 1
        na = a1 + (cont - 1) * razao
        print("O {:2}° termo da sua PA é: {}".format(cont, na))
else:
    print("Tudo bem! Tenha um bom dia!")
print("FIM!")"""