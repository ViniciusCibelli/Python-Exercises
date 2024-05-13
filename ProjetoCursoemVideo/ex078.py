maior = menor = 0
valores = []
for cont in range(0, 5):
    resposta = valores.append(int(input(f"Digite um valor na posição {cont}: ")))

    if cont == 0:
        maior = menor = valores[cont]

    else:
        if valores[cont] > maior:
            maior = valores[cont]
        if menor > valores[cont]:
            menor = valores[cont]

print(f"Os valores digitados foram: {valores}")

print(f"O \033[32mmaior valor\033[m digitado foi {maior}, nas posições ", end='')
for index, valor in enumerate(valores):
    if valor == maior:
        print(f"{index} ", end='')
print()

print(f"O \033[31mmenor valor\033[m digitado foi {menor}, nas posições ", end='')
for index, valor in enumerate(valores):
    if valor == menor:
        print(f"{index} ", end='')
print()

print("Fim!")
