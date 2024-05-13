# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.

print(f"{'-=' * 10} TÁBUADA {'-=' * 10}")
print("\033[31mDigite qualquer número negativo para encerrar!\033[m")
print(f"{'-=' * 25}")
contador = numero = 0
numero = int(input("\033[34mDigite o número que você deseja saber a tabuada:\033[m "))
while True:
    print(f"{contador:2} x {numero} = {contador * numero}")
    contador += 1
    if contador == 11:
        numero = int(input("\033[34mDigite o número que você deseja saber a tabuada:\033[m "))
        contador = 0
    if numero < 0:
        break
print(f"{'-=' * 25}")
print("\033[33mEncerrando... Finalizado, volte sempre!\033[m")
