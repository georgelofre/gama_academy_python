import random
lista = [
'Ana Paula Santos',
'Anderson Teixeira',
'Beatriz Cardozo',
'Bruna Rafael',
'Bruno Carvalho',
'Bruno fernandes da costa',
'Bruno Lima',
'Divino alonso',
'Edson Almeida',
'Erick Bontempo'
]

grupos = [[], [], [], [], []]

for c in range(0, 5):
    if len(lista) > 2:
        for z in range(0, 2):
            num = random.randint(0, len(lista)-1)
            print(num)
            grupos[c].append(lista[num][:])
            del lista[num]
            print(f'Nova lista: {lista}\n e a quantidade: {len(lista)}')
            print(grupos)
    else:
        grupos[4].append(lista[0])
        grupos[4].append(lista[1])
print('+=' *20)
print(grupos)






