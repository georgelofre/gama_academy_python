n1 = float(input('Qual nota 1? '))
n2 = float(input('Qual nota 2? '))
media = (n1 + n2)/2
if media == 10:
    print('Aprovado com distinção!')
elif 10 > media >= 7:
    print('Aprovado!')
elif media < 7:
    print('Reprovado!')
