lista = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90)
print('=' * 40)
print(f"{'LISTA DE PREÇOS':^40}")
print('=' * 40)
z = 0
for c in lista:
    if z == 0:
        print(f'{lista[z]:.<30}', end='')
    elif z == 1:
        print(f'R$ {lista[z]:>5.2f}')
    else:
        if z % 2 == 0:
            print(f'{lista[z]:.<30}', end='')
        else:
            print(f'R$ {lista[z]:>5.2f}')
    z += 1

