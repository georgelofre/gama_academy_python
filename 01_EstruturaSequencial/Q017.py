import math
tamanho = float(input('Digite a área a ser pintada: '))
litros = (tamanho / 6) * 1.1
print(f'Serão necessários {litros} litros.')
print('-------')
latas = math.ceil(litros / 18)
print(f'Se forem latas: Serão necessárias {latas} latas.')
valor1 = latas * 80.00
print(f'O valor a ser pago é de R$ {valor1:.2f}.')
print('-------')
galoes = math.ceil((litros / 3.6) * 1.1)
print(f'Se forem galões: Serão necessários {galoes} galões.')
valor2 = galoes * 25.00
print(f'O valor a ser pago é de R$ {valor2:.2f}.')
print('-------')
latas2 = litros // 18
resto = litros % 18
galoes2 = math.ceil(resto / 3.6)
valor3 = latas2 * 80.00
valor4 = galoes2 * 25.00
print(f'Misturando temos a quantidade de Latas: {int(latas2)} e o valor é R$ {valor3:.2f} e de galões: {galoes2} e o valor é R$ {valor4:.2f}.')

