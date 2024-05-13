frase = input("Digite uma frase: ").split()
novafrase = ''.join(frase)
i = 0
eh_palindromo = True
for c in range(len(novafrase)-1, -1, -1):
    print(novafrase[c])
    print(novafrase)
    print(novafrase[i])
    if novafrase[c] != novafrase[i]:
        eh_palindromo = False
    break
    i += 1
if eh_palindromo:
    print("É")
else:
    print("NÃO É")
print(i)