jog = {}
jog['Nome'] = str(input('Nome do jogador: '))
jog['Partidas'] = int(input('Quantas partidas ele jogou: '))
jog['gols'] = []
for c in range(1, jog['Partidas']+1):
    jog['gols'].append(int(input(f'Quantos gols ele fez na partida {c}: ')))
cont_gol = 0
for z in range(0, len(jog['gols'])):
    cont_gol += jog['gols'][z]
jog['total'] = cont_gol
print('+=+'*20)
print(jog)
print('+=+'*20)
for k,v in jog.items():
    print(f'{k} ==> {v}.')
print('+=+'*20)
print(f'O jogador {jog["Nome"]} jogou {jog["Partidas"]} partidas.')
for i, v in enumerate (jog['gols']):
    print(f'Na partida {i+1} ele fez {v} gols')
