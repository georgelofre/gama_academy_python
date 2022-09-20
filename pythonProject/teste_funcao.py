def numero_int(a):
    if str(a).isdigit():
        int(a)
    else:
        print('Não há so números.')



cod_produto = input('\nDigite o código do produto a ser adicionado: ')
while cod_produto.isdigit() != True:
    print('tem letras')
    cod_produto = input('\nDigite o código do produto a ser adicionado: ')
