# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome dos alunos e
# escrevendo na tela o nome do escolhido.

import random
aluno1 = str(input("Digite o nome do aluno 1: "))
aluno2 = str(input("Digite o nome do aluno 2: "))
aluno3 = str(input("Digite o nome do aluno 3: "))
aluno4 = str(input("Digite o nome do aluno 4: "))
print("O aluno sorteado para apagar o quadro foi o: {0}!".format(random.choice([aluno1, aluno2, aluno3, aluno4])))
