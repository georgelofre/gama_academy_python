n1 = int(input('Digite o 1º número:'))
n2 = int(input('Digite o 2º número:'))
n3 = int(input('Digite o 3º número:'))
maior = menor = n1
if n2 > n1 and n2 > n3:
    maior = n2
elif n3 > n1 and n3 > n2:
    maior = n3
if n2 < n1 and n2 < n3:
    menor = n2
elif n3 < n1 and n3 < n2:
    menor = n3
if n1 != maior and n1 != menor:
    meio = n1
elif n2 != maior and n2 != menor:
    meio = n2
else:
    meio = n3
print(f'O ordem é {menor, meio, maior}.')