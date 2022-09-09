from random import randint
import operator

ordem = dict()
lista = []

ordem['jogador1'] = randint(1, 6)
ordem['jogador2'] = randint(1, 6)
ordem['jogador3'] = randint(1, 6)
ordem['jogador4'] = randint(1, 6)
print('Valores sorteados: ')
for k,v in ordem.items():
    print(f'O {k} tirou {v}.')
print('='*30)
ranking = []
ranking = sorted(ordem.items(), key=operator.itemgetter(1), reverse=True)
print(ranking)
