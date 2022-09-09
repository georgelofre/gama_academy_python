lista = []
for c in range (0,5):
    lista.append(int(input('Digite um número: ')))
maior = max(lista)
menor = min(lista)
pos_maior = lista.index(maior)
pos_menor = lista.index(menor)
print(lista)
print(f'A posição do maior: {pos_maior+1}.')
print(f'A posição do menor: {pos_menor+1}.')