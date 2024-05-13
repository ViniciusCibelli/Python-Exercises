def jogar_advinhacao():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    from random import randint
    numero_secreto = randint(1, 100)
    print("""
    [1] Fácil   - 15 tentativas
    [2] Médio   - 10 tentativas
    [3] Dificil - 5  tentativas""")

    while True:
        escolha = int(input("Escolha a dificuldade do jogo: "))
        if escolha == 1:
            total_de_tentativas = 15
            pontos = 750
            break
        elif escolha == 2:
            total_de_tentativas = 10
            pontos = 500
            break
        elif escolha == 3:
            total_de_tentativas = 5
            pontos = 250
            break
        else:
            print("Opção errada! Tente novamente...")

    print(f"Você tem {pontos} pontos!")

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute = int(input("Digite um número entre 1 e 100: "))

        if chute < 1 or chute > 100:
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior   = chute >  numero_secreto
        menor   = chute <  numero_secreto

        if acertou:
            print("Você \033[32macertou\033[m!")
            break
        else:
            if maior:
                print("Você errou! Tente um número \33[31mmenor\33[m.")

            elif menor:
                print("Você errou! Tente um número \33[34mmaior\33[m.")

            print("Você \33[33mperdeu\33[m 50 pontos!")
            pontos -= 50

    print(f"O número secreto é {numero_secreto}")
    print(f"Você acabou o jogo com {pontos} pontos!")
    print("Fim do jogo")


if __name__ == "__main__":
    jogar_advinhacao()
