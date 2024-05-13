# Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço formal
# – 3x ou mais no cartão: 20% de juros

preco = float(input("Digite o valor do produto R$"))
print("""[1] - À vista dinheiro/cheque: 10% de desconto
[2] - À vista no cartão: 5% de desconto
[3] - Em até 2x no cartão: preço formal
[4] - 3x ou mais no cartão: 20% de juros""")
opcao = int(input("Escolha uma opção de pagamento: "))
parcela = preco / 2
if opcao == 1:
    preco = preco - (preco * 0.1)
    print("Com 10% de desconto você irá pagar {0:.2f} reais".format(preco))
elif opcao == 2:
    preco = preco - (preco * 0.05)
    print("Com 5% de desconto você irá pagar {0:.2f} reais".format(preco))
elif opcao == 3:
    print("Parcelando duas vezes, o produto continuará custando {0:.2f} reais e cada parcela custara {1:.2f} reais".format(preco, parcela))
elif opcao == 4:
    preco1 = preco + (preco * 0.2)
    parcela = preco / 3
    print("Parcelando em três vezes, o preço passa de R${0:.2f} para {1:.2f} reais e cada parcela custará {2:.2f} reais".format(preco, preco1, parcela))
else:
    print("Opção NÃO encontrada! Tente novamente!")
