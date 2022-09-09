import random
print('='*30)
print(f'{"JOGO DA MEGA SENA":^30}')
print('='*30)
qtd = int(input('Quantos jogos vôce quer jogar? '))
lista_geral = []
lista = []
for i in range(0, qtd):
    while True:
        num = random.randint(1, 60)
        if num not in lista:
            lista.append(num)
        if len(lista) == 6:
            break
    print(lista)
    lista_geral.append(lista[:])
    lista.clear()
print(lista_geral)

