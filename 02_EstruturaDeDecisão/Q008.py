n1 = float(input('Digite o 1º produto: '))
n2 = float(input('Digite o 2º produto: '))
n3 = float(input('Digite o 3º produto: '))
menor = n1
produto = 1
if n2 < n1 and n2 < n3:
    menor = n2
    produto = 2
elif n3 < n1 and n3 < n2:
    menor = n3
    produto = 3
print(f'O menor preço é do produto {produto} de valor R$ {menor}.')