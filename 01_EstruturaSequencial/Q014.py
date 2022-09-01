peso = float(input('Digite o peso em kg se foi maior que 50kg: '))
excesso = peso - 50
multa = excesso * 4.0
print(f'A quantidade em excesso é de {excesso:.2f}kg e a multa é de R$ {multa:.2f}.')