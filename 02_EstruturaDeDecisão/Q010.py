turno = str(input('Em que turno você estuda? M-matutino ou V-Vespertino ou N- Noturno: '))
if turno in "M":
    print('Bom dia!')
elif turno in "V":
    print('Boa tarde!')
elif turno in "N":
    print('Boa noite!')
else:
    print('Valor inválido!')