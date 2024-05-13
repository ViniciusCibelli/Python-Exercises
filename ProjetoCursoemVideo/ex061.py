# Refaça o DESAFIO 51:
# Lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.

from time import sleep
print("{} GERADOR DE PAs: {}".format('-=' * 5, '-=' * 5))
sleep(1)
a1 = int(input("Digite qual o primeiro valor da sua PA: "))
razao = int(input("Digite qual a razão da sua PA: "))
cont = 0
while cont != 10:
    cont += 1
    an = a1 + (cont - 1) * razao
    print("O {:2}° termo da sua PA é: {}".format(cont, an))
print("FIM")
