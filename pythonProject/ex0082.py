lista = []
while True:
    num = int(input('Digite um número: [999 para parar] '))
    if num == 999:
        break
    lista.append(num)
pares = []
impares = []
for c in range(0, len(lista)):
    if lista[c] % 2 == 0:
        pares.append(lista[c])
    else:
        impares.append(lista[c])
print(lista)
print(pares)
print(impares)