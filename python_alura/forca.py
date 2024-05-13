import random

def initial_message():
    print("*********************************")
    print("Bem vindo ao jogo da Forca!")
    print("*********************************")
def get_secret_word():
    file = open("palavrinhas.txt", "r")
    words = []

    for line in file:
        line = line.strip()
        words.append(line)
    file.close()

    number = random.randrange(0, len(words))
    secret_word = words[number].upper()
    return secret_word
def get_winner():
        print("Parabéns, você ganhou!")
        print("       ___________      ")
        print("      '._==_==_=_.'     ")
        print("      .-\\:      /-.    ")
        print("     | (|:.     |) |    ")
        print("      '-|:.     |-'     ")
        print("        \\::.    /      ")
        print("         '::. .'        ")
        print("           ) (          ")
        print("         _.' '._        ")
        print("        '-------'       ")
def get_loser(secret_word):
    print(f"A palavra secreta era: {secret_word}\n")
    print("Puxa, você foi enforcado!")
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")
def hang_scratch(mistakes):
    print("  _______     ")
    print(" |/      |    ")

    if(mistakes == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(mistakes == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(mistakes == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(mistakes == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(mistakes == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(mistakes == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (mistakes == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def jogar_forca():
    initial_message()

    secret_word = get_secret_word()

    hits = ["_" for letter in secret_word] #list comprehensions
    print(hits)

    hanged = acertou = False
    mistakes = 0

    while not hanged and not acertou:

        guess = input("Qual letra? ").strip().upper()

        if(guess in secret_word):
            index = 0
            for letter in secret_word:
                if guess == letter:
                    hits[index] = letter
                index += 1
        else:
            mistakes += 1
            hang_scratch(mistakes)

        hanged = mistakes == 7
        acertou = "_" not in hits
        print(hits)

    if acertou:
        get_winner()
    else:
        get_loser(secret_word)

if __name__ == "__main__":
    jogar_forca()
