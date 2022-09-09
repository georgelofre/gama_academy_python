lista = []
c = 0
while True:
    novo = int(input('Digite um número: '))
    if c == 0 or novo > lista[-1]:
        lista.append(novo)
    else:
        z = 0
        while z < len(lista):
            if novo <= lista[z]:
                lista.insert(z, novo)
                break
            z += 1
    print(lista)
    c += 1
    print('====================================')
    if len(lista) == 6:
        break
print(lista)
