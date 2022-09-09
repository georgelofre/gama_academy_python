nova = str(input('Digite uma frase que contenha parênteses em qualquer ordem: '))
abertos = []
fechados = []
par_abertos = nova.count('(')
par_fechados = nova.count(')')
for c in range(0, len(nova)):
    if nova[c] == '(':
        abertos.append(c)
    elif nova[c] == ')':
        fechados.append(c)
if par_abertos != par_fechados:
    print('O número de parênteses está incorreto!')
else:
    cont = 0
    for num in range (0, len(abertos)):
        if abertos[num] < fechados[num]:
            cont += 1
    if cont == par_abertos:
        print("O números de parênteses está correto!")

