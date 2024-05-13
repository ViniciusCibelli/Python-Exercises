# Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
# calcule seu Índice de Massa Corporal (IMC) e mostre seu status,
# de acordo com a tabela abaixo:
# – IMC abaixo de 18,5: Abaixo do Peso
# – Entre 18,5 e 25: Peso Ideal
# – 25 até 30: Sobrepeso
# – 30 até 40: Obesidade
# – Acima de 40: Obesidade Mórbida

altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))
IMC = peso / (altura * altura)
print("Seu IMC é {0:.1f}".format(IMC))
if IMC <= 18.5:
    print("Você está \033[31mabaixo do peso\033[m ideal")
elif IMC > 18.5 and IMC <= 25:
    print("Você está no \033[32mpeso ideal\033[m")
elif IMC > 25 and IMC <= 30:
    print("Você está com \033[33msobrepeso\033[m")
elif IMC > 30 and IMC <= 40:
    print("Você está com \033[34mobesidade\033[m")
else:
    print("Você está com obesidade mórbida")
