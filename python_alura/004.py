secret_number = 42
total_tentativas = 3

print('-=' * 20)
print("BEM VINDO AO JOGO DE ADIVINHAÇÃO!")
print('-=' * 20)

for rodada in range(1, total_tentativas + 1):
    print(f"Tentativa {rodada} de {total_tentativas}")
    chute = int(input("Digite um número de 0 - 100: "))

    if chute < 1 or chute > 100:
        print("Digite um número ENTRE 0 e 100!")
        continue

    acertou = chute == secret_number
    maior   = chute >  secret_number
    menor   = chute <  secret_number

    if acertou:
        print("Parabéns, você acertou!")
        break

    elif maior:
        print("Que pena, você errou!")
        print("Tente um número MENOR!")

    elif menor:
        print("Que pena, você errou!")
        print("Tente um número MAIOR!")

print("FIM")
