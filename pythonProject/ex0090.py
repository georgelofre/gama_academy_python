aluno = dict()
aluno['nome'] = str(input('Digite o nome do aluno: '))
aluno['media'] = float(input('Qual a média: '))
if aluno['media'] >= 7.00:
    aluno['situacao'] = 'Aprovado'
else:
    aluno['situacao'] = 'Reprovado'
for k,v in aluno.items():
    print(f'{k} ==> {v}.')
