matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for lin in range(0, 3):
    for col in range(0, 3):
        matriz[lin][col] = int(input(f'Digite um número para [{lin}][{col}]: '))
print(matriz)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end=' ')
    print('')





'''matriz_1 = [[], [], []]
for l1 in range(0, 3):
    matriz_1[l1].append(int(input('Digite um número: ')))
matriz_2 = [[], [], []]
for l2 in range(0, 3):
    matriz_2[l2].append(int(input('Digite um número: ')))
matriz_3 = [[], [], []]
for l3 in range(0, 3):
    matriz_3[l3].append(int(input('Digite um número: ')))
print(matriz_1)
print(matriz_2)
print(matriz_3)
'''