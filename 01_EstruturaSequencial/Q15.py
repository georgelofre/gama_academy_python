ganho = float(input('Quanto você ganha por hora: '))
qtd_horas = int(input('Quantas horas trabalhou nesse mês: '))
bruto = ganho*qtd_horas
irpf = 0.11 * bruto
inss = 0.08 * bruto
sind = 0.05 * bruto
liquido = bruto - (irpf + inss + sind)
print(f'O seu salário bruto foi de R$ {bruto:.2f}.')
print(f'O valor pago de irpf é de R$ {irpf:.2f}')
print(f'O valor pago de inss é de R$ {inss:.2f}')
print(f'O valor pago de sindicato é de R$ {sind:.2f}')
print(f'O valor pago de salário liquido é de R$ {liquido:.2f}')
