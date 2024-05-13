from random import randint
numero = randint(0, 10)
print("-=" * 20)
print("JOGO DE ADVINHAÇÃO")
print("-=" * 20)
while True:
    resposta = int(input("Escolha um número de 0 - 10: "))
    if resposta == numero:
        print("\033[32mPARÁBENS, VOCÊ ACERTOU!!\033[m")
        print(f"O computador pensou em {numero}")
        break
    else:
        print("\033[31mVOCÊ ERROU! TENTE NOVAMENTE!\033[m")
        if resposta > numero:
            print("Pense em um número \033[33mmenor\033[m!")
        elif resposta < numero:
            print("Pense em um número \033[34mmaior\033[m!")
print("FIM!")
