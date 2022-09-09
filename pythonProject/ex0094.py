pessoa = {}
lista = []
while True:
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: '))[0].upper().strip()
        if pessoa['sexo'] in "FM":
            break
        else:
            print('ERRO! Responda apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    lista.append(pessoa.copy())
    cont = str(input('Quer continuar? [S/N] '))[0].upper().strip()
    if cont == 'N':
        break
print(lista)
print(f'Foram cadastradas {len(lista)} pessoas.')
soma_id = 0
media_id = 0
for c in range(0, len(lista)):
    soma_id += lista[c]['idade']
    media_id = float(soma_id / len(lista))
print(f'A média de idade foi de {media_id} anos.')
mulher = []
for c in range(0, len(lista)):
    if lista[c]['sexo'] == 'F':
        mulher.append(lista[c]['nome'])
print(f'A lista de mulheres é: {mulher}.')
acima = []
print('As pessoas com idade acima da média: ', end='')
for c in range(0, len(lista)):
    if lista[c]['idade'] > media_id:
        print(lista[c]['nome']+' ', end='')


