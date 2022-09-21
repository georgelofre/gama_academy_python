def fatorial(numero, show):
    """ Aqui vai o calculo!"""
    fat = numero
    for c in range(numero - 1, -1, -1):
        fat = fat * c
    print(fat)
    if show in "Ss":
        print(help(fatorial))

num = int(input('Digite um número: '))
mostrar = str(input('Deseja mostrar o calculo? '))
fatorial(num, mostrar)
