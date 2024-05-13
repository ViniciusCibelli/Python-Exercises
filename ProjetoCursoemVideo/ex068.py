from random import randint
computador = randint(0, 10)
numero = ''
opcao = ''
contador = 0
while True:
    numero = int(input("Diga um valor: "))
    opcao = str(input("Par ou Ímpar? [P/I] ")).strip().upper()
    if opcao == 'P' and (computador + numero) % 2 != 0:
        print("\033[31mVocê perdeu!\033[m")
        break
    elif opcao == 'I' and (computador + numero) % 2 == 0:
        print("\033[31mVocê perdeu!\033[m")
        break
    else:
        print(f"O computador jogou {computador}, {computador + numero} é {opcao} e \033[32mvocê ganhou!\033[m")
        contador += 1
print("Encerrando...")
print(f"Você ganhou {contador} vezes!")
print("Processo finalizado, volte sempre!")