lista = [6, 4, 8, 6]
def dobra(list1):
    cont = 0
    while cont < len(list1):
        list1[cont] = list1[cont] * 2
        cont += 1
    print(f'Lista dobrada {list1}')
dobra(lista)

