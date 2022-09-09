lista = []
aluno = []
while True:
    aluno.append(str(input('Nome do aluno: ')))
    aluno.append(float(input('Nota 01: ')))
    aluno.append(float(input('Nota 02: ')))
    lista.append(aluno[:])
    aluno.clear()
    cont = str(input('Quer continuar? [S/N] '))[0].upper()
    if cont in 'N':
        break
print('+=+'*20)
print(f'{"Número":<10}{"NOME":<15}{"MÉDIA":>10}')
print('+=+'*20)
for c in range(0, len(lista)):
    print(f'{c:<10}{lista[c][0]:<15}{(lista[c][1] + lista[c][2])/2:>10.2f}')
while True:
    mostrar = int(input('Mostrar notas de qual alunno: [999 p/ parar] '))
    if mostrar == 999:
        break
    print(f'Nota 01: {lista[mostrar][1]}\nNota 02: {lista[mostrar][2]}')
