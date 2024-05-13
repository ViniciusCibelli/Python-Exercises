# Crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final, de acordo com a média atingida:
# – Média abaixo de 5.0: REPROVADO
# – Média entre 5.0 e 6.9: RECUPERAÇÃO
# – Média 7.0 ou superior: APROVADO

p1 = float(input("Digite a nota da sua primeira prova: "))
p2 = float(input("Digite a nota da sua segunda prova: "))
media = (p1 + p2) / 2
if media < 5:
    print("Sua média foi: {} e infelizmente você foi \033[31mREPROVADO\033[m!".format(media))
    print("Estude mais!")
elif media >= 5 and media <= 6.9:
    print("Sua média foi {}, você está de \033[33mRECUPERAÇÃO\033[m !".format(media))
    print("Estude mais!")
else:
    print("Sua média foi {}, parabéns você foi \033[32mAPROVADO\033[m".format(media))
    print("Continue estudando desse jeito!")