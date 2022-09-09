jog = {}
todos = []
while True:
    jog['Nome'] = str(input('Nome do jogador: '))
    jog['Partidas'] = int(input('Quantas partidas ele jogou: '))
    jog['gols'] = []
    jog['total'] = 0
    for c in range(1, jog['Partidas']+1):
        gol = (int(input(f'Quantos gols ele fez na partida {c}: ')))
        jog['gols'].append(gol)
        jog['total'] += gol
    todos.append(jog.copy())
    cont = str(input('Quer continuar? [S/N] '))[0].upper().strip()
    while cont not in 'SsNn':
        cont = str(input('Quer continuar? [S/N] '))[0].upper().strip()
    if cont == 'N':
        break
print(todos)
print('*'*30)
print(f'{"Cód":^5}{"Nome":<10}{"Gols":<10}{"Total":<5}')
print('*'*30)
for i in range(0, len(todos)):
    print(f'{i+1:^5}{todos[i]["Nome"]:<10}{todos[i]["gols"]}{todos[i]["total"]:>5}')
while True:
    mostrar = int(input('Mostrar notas de qual jogador: [999 p/ parar] ')) - 1
    if mostrar == 998:
        break
    print(f'Nome: {todos[mostrar]["Nome"]}')
    print(f'Número de jogos: {todos[mostrar]["Partidas"]}')
    print(f'Gols: {todos[mostrar]["gols"]}')
    print(f'Total de gols: {todos[mostrar]["total"]}')

