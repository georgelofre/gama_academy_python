lista = []
while True:
    novo = int(input('Digite um número: '))
    if novo not in lista:
        lista.append(novo)
    else:
        print('Número já existente!')
    cont = str(input('Quer continuar? [S/N] '))
    if cont in 'Nn':
        break
lista.sort()
print(f'{lista}')


