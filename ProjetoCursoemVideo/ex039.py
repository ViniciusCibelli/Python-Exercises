# Faça um programa que leia o ano de nascimento de um jovem e informe
# De acordo com a sua idade, se ele ainda vai se alistar ao serviço militar
# Se é a hora exata de se alistar ou se já passou do tempo do alistamento
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo
"""
nascimento = int(input("Digite o ano do seu nascimento: "))
quantofalta = 18 - (2021 - nascimento)
quantopassou = (2021 - nascimento) - 18
if 2021 - nascimento == 18:
    print("Você deve fazer a inscrição para o serviço militar esse ano!")
elif 2021 - nascimento > 18:
    print("Você já passou {} anos da idade de servir o exercito, procure se informar!".format(quantopassou))
elif 2021 - nascimento < 18:
    print("Você ainda é novo de mais para o serviço militar. Daqui {} ano(s) você poderá servir!".format(quantofalta))
"""

from datetime import date
atual = date.today().year
nascimento = int(input("Em que ano você nasceu? "))
idade = atual - nascimento
saldo = 18 - idade
print("Quem nasceu em {}, tem {} anos atualmente!".format(nascimento, idade))
if idade == 18:
    print("Você deve fazer o alistamento esse ano!")
elif idade < 18:
    print("Você ainda não chegou na idade de se alistar!")
    print("Ainda falta(m) {} ano(s)!".format(saldo))
elif idade > 18:
    saldo = idade - 18
    print("Você já passou {} da idade de se alistar, se informe imediatamente!".format(saldo))
