import datetime
pessoa = {}
pessoa['nome'] = str(input('Nome: '))
pessoa['nascimento'] = int(input('Ano de nascimento: '))
pessoa['ctps'] = int(input('Carteira de trabalho (0 p/ não tem): '))
atual = datetime.date.today().year
if pessoa['ctps'] != 0:
    pessoa['contratacao'] = int(input('Ano de contratação: '))
    pessoa['salário'] = float(input('Salário: '))
    pessoa['Anos p/ aposentadoria'] = 65 - (atual - pessoa['nascimento'])
for k, v in pessoa.items():
    print(f'{k} ==> {v}.')