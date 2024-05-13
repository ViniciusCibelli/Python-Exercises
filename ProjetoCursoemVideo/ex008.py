# Escreva um programa que leia um valor escrito em metros e o exiba convertido em CENTIMETROS e MILIMETROS

dm = float(input("Digite um valor em metros "))
dc = dm*100
dmm = dc*10 # dmm = dm*1000
print('='*30)
print("{0} metro(s) é/são: {1} centimetros \nO mesmo valor equivale a {2} milimetros".format(dm, dc, dmm))
