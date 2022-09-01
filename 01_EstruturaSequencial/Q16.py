import math
tamanho = float(input('Digite a área a ser pintada: '))
litros = tamanho / 3
print(f'Serão necessários {litros} litros.')
print('-------')
latas = litros / 18
print(f'Serão necessárias {math.ceil(latas)} latas.')
print('-------')
valor = latas * 80.00
print(f'O valor a ser pago é de R$ {valor:.2f}.')