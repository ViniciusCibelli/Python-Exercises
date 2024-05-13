# A Confederação Nacional de Natação precisa de um programa que leia o ano
# de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# – Até 9 anos: MIRIM
# – Até 14 anos: INFANTIL
# – Até 19 anos: JÚNIOR
# – Até 25 anos: SÊNIOR
# – Acima de 25 anos: MASTER

from datetime import date
atual = date.today().year
nasc = int(input("Qual é o ano do seu nascimento: "))
idade = atual - nasc
print("Quem nasceu em {}, agora tem {} anos".format(nasc, idade))
if idade <= 9:
    print("Você é considerado um atleta \033[36mMIRIM\033[m!")
elif idade <= 14 and idade > 9:
    print("Você é considerado um atleta \033[33mINFANTIL\033[m!")
elif idade <= 19 and idade > 14:
    print("Você é considerado um atleta \033[31mJÚNIOR\033[m!")
elif idade <= 25 and idade > 19:
    print("Você é considado um atleta \033[32mSENIOR\033[m!")
else:
    print("Você é considerado um atleta \033[35mMASTER\033[m!")
