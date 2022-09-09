tupla = (
    str(input('Digite uma palavra: ')),
    str(input('Digite uma palavra: ')),
    str(input('Digite uma palavra: '))
)
for palavra in tupla:
    print(f'As vogais da palavra {palavra} são: ')
    for c in range(0, len(palavra)):
        if palavra[c].lower() in 'aeiou':
            print(palavra[c], end=' ')
    print('')

