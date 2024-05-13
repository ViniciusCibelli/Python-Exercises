# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

Tc = float(input("Digite uma temperatura em °C: "))
Tf = (Tc*1.8) + 32
print("="*30)
print("\033[34m{0:.1f}ºC\033[m, carresponde a \033[35m{1:.1f}ºF\033[m!".format(Tc, Tf))
