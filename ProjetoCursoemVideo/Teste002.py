n = int(input('Quantos termos quer mostrar da sequência: '))
c = 0
segundo = c
proximo = 1
print('0', end='')
while c <= n - 2:
    print(f' → {proximo}', end='')
    c += 1
    proximo += segundo
    segundo = proximo - segundo
print(' → FIM')
