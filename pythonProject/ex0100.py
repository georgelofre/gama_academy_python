import random

numeros = []
def sorteia(x):
    for c in range(0, 5):
        numeros.append(random.randint(0, 10))
    print(x)

def somaPar(z):
    soma_par = 0
    for i, v in enumerate(z):
        if v % 2 == 0:
            soma_par = soma_par + v
    print(f'A soma dos valores pares é {soma_par}.')
sorteia(numeros)
somaPar(numeros)