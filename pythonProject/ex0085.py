lista = []
while True:
    num = (int(input('Digite um número: ')))
    if num % 2 == 0:
        lista.insert(0, num)
    else:
        lista.append(num)
    if len(lista) == 7:
        break
print(lista)
print('A lista de números pares é: ', end='')
for c in range(0, 7):
    if lista[c] % 2 == 0:
        print(lista[c], end=' ')
print('')
print('A lista de números ímpares é: ', end='')
for i in range(0, 7):
    if lista[i] % 2 != 0:
        print(lista[i], end=' ')


