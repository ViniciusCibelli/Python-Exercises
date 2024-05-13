from advinhacao import jogar_advinhacao
from forca import jogar_forca

print("*********************************")
print("Bem vindo, escolha o seu jogo!")
print("*********************************")
#def escolhe_jogo():
print("[1] Forca ou [2] Advinhação")
escolha = int(input("Escolha qual jogo você deseja jogar: "))

if escolha == 1:
    print("Jogando Forca")
    jogar_forca()

elif escolha == 2:
    print("Jogando Advinhação")
    jogar_advinhacao()


#if __name__ == "__main__":
#   escolhe_jogo()