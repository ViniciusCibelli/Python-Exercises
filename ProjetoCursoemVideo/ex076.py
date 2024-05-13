# Crie um programa que tenha uma tupla única com nomes de produtos
# e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

tabela = ('Lápis', 1, 'Borracha', 1.5, 'Caderno', 5)
print('-=-' * 15)
print(f"{'LISTAGEM DE PRODUTOS':^40}")
print('-=-' * 15)
for posicao in range(0, len(tabela)):
    if posicao % 2 == 0:
        print(f"{tabela[posicao]:.<30}", end='')
    else:
        print((f"R${tabela[posicao]:>7.2f}"))
