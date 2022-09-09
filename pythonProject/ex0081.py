lista = []
while True:
    num = int(input('Digite um número: [999 para parar] '))
    if num == 999:
        break
    lista.append(num)
print('==============================')
print(lista)
print(f'Foram digitados {len(lista)} números.')
cont_5 = 0
lista_index5 = []
for c in range (0, len(lista)):
    if lista[c] == 5:
        cont_5 += 1
        lista_index5.append(c)
print(f'O número 5 foi digitado {cont_5} vezes, nas posições: {lista_index5}.')
lista.sort(reverse=True)
print(f'Na ordem decrescente fica: {lista}')
