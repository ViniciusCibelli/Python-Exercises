# Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso

from time import sleep
operacao = 0
numero1 = float(input("Digite um número: "))
numero2 = float(input("Digite outro número: "))
while operacao != 5:
    print("""[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa""")
    operacao = int(input("Escolha qual operação deseja fazer: "))
    if operacao == 1:
        print("A soma dos valores citados é: {}".format(numero1 + numero2))
    elif operacao == 2:
        print("A multiplicação dos valores citados é: {}".format(numero1 * numero2))
    elif operacao == 3:
        if numero1 > numero2:
            print("O maior valor citado é: {}".format(numero1))
        else:
            print("O maior valor citado é: {}".format(numero2))
    elif operacao == 4:
        numero1 = float(input("Digite um número: "))
        numero2 = float(input("Digite outro número: "))
    elif operacao == 5:
        print("Finalizando...")
    else:
        print("ERRO, TENTE NOVAMENTE!")
    print('-=' * 20)
    sleep(2)
print("Até mais, tenha um bom dia!")
