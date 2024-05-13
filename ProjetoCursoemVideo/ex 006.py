# Crie um algoritimo que leia um número e mostre o seu dobro, trilho e raiz quadrada

n = int(input("Digite um número "))
d = n*2
t = n*3
rq = n**(1/2)
print('='*30)
print("O número escolhido foi: \033[33m{0}\033[m \nO seu dobro é: \033[44m{1:.2f}\033[m \nO seu triplo é: \033[45m{2:.2f}\033[m \nE, sua raiz quadrada é: \033[31m{3:.2f}\033[m".format(n, d, t, rq))
# print("O número escolhido foi: {0}, o seu dobro é: {1:.2f}, o seu triplo é: {2:.2f} e sua raiz quadrada é: {3:.2f}".format(n, d, t, rq))
# # print("O número escolhido foi: {0}, o seu dobro é: {1:.2f}, o seu triplo é: {2:.2f} e sua raiz quadrada é: {3:.2f}".format(n, n*2, n*3, n**(1/2)))