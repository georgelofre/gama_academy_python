matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for lin in range(0, 3):
    for col in range(0, 3):
        matriz[lin][col] = int(input(f'Digite um número para [{lin}][{col}]: '))
print(matriz)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end=' ')
    print('')
soma_par = 0
for l in range(0, 3):
    for c in range(0, 3):
        if matriz[l][c] % 2 == 0:
            soma_par += matriz[l][c]
    print('')
print(f'A soma dos valores pares é de {soma_par}.')
soma_3col = 0
for c in range(0, 3):
    soma_3col += matriz[c][2]
print(f'A soma dos valores da terceira coluna é {soma_3col}.')
for c in range(0, 3):
    if c == 0:
        maior = matriz[1][0]
    else:
        if matriz[1][c] > maior:
            maior = matriz[1][c]
print(f'O maior valor da segunda linha é {maior}.')
