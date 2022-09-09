lista = []
dados = []
lista_maior = []
lista_menor = []
nomes_maior = []
nomes_menor = []
while True:
    dados.append(str(input('Qual o nome?')))
    dados.append((int(input('Qual o peso?'))))
    lista.append(dados[:])
    dados.clear()
    cont = str(input('Quer continuar? [S/N]'))
    if cont in "Nn":
        break
print(lista)
print(f'Foram cadastradas {len(lista)} pessoas.')
for h in range(0, len(lista)):
    lista_maior.append(lista[h][1])
    lista_menor.append(lista[h][1])
lista_maior.sort()
print('A lista do mais leve para o mais pesado é: ', end='')
for c in range(0, len(lista)):
    for z in range(0, len(lista)):
        if lista[z][1] == lista_maior[c]:
            nomes_maior.append(lista[z][0])
print(nomes_maior)
lista_menor.sort(reverse=True)
print('A lista do mais pesado para o mais leve é: ', end='')
for c in range(0, len(lista)):
    for z in range(0, len(lista)):
        if lista[z][1] == lista_menor[c]:
            nomes_menor.append(lista[z][0])
print(nomes_menor)
