produtos = {}

while True:
    print('=' * 30)
    print('=' * 30)
    print(f'{"SEJA BEM VINDO!":^30}')
    print('=' * 30)
    print('=' * 30)
    print('Para entrar no programa digite [1]')
    print('Para sair do programa digite [2]')
    num = int(input("Digite o que deseja: "))
    while num != 1 and num != 2:
        num = int(input('Código inválido! Digite novamente: '))
    if num == 1:
        while True:
            print('=' * 30)
            print('=' * 30)
            print(f'{"MENU DE NAVEGAÇÃO":^30}')
            print('=' * 30)
            print('=' * 30)
            print('Bem vindo ao menu de navegação! Observe as opções abaixo e escolha a que deseja!')
            print('1. Cadastro')
            print('2. Vendas')
            print('3. Relatório')
            print('4. Voltar')
            num1 = int(input("Digite o que deseja: "))
            if num1 == 1:
                while True:
                    print('=' * 30)
                    print('=' * 30)
                    print(f'{"MENU DE CADASTRO":^30}')
                    print('=' * 30)
                    print('=' * 30)
                    print('O que deseja fazer?')
                    print('1. Cadastrar produto.')
                    print('2. Listar produtos cadastrados.')
                    print('3. Deleção de produtos')
                    print('4. Voltar')
                    num = int(input("Digite o que deseja: "))
                    if num == 1:
                        while True:
                            print('=' * 30)
                            print('=' * 30)
                            nome = str(input('Digite o nome do produto: '))
                            estoque = int(input('Qual a quantidade: '))
                            preco = float(input('Qual o preço: R$ '))
                            produtos[nome] = [estoque, preco]
                            print(produtos.keys(), produtos.values())
                            print('=' * 30)
                            novo = str(input('Cadastrar novo produto? [S/N]'))
                            if novo in 'Nn':
                                print('.\n.\n.\n')
                                break
                    elif num == 2:
                        print('Em construção...')
                    elif num == 3:
                        print('Em construção...')
                    elif num == 4:
                        print('.\n.\n.\n')
                        break
            elif num1 == 2:
                print('=' * 30)
                print('=' * 30)
                print(f'{"MENU DE VENDAS":^30}')
                print('=' * 30)
                print('=' * 30)
                print('O que deseja fazer?')
                print('1. Listar produtos cadastrados.')
                print('2. Adição de produtos ao carrinho.')
                print('3. Finalização da venda do carrinho')
                print('4. Voltar')
                num = int(input("Digite o que deseja: "))
                if num == 1:
                    while True:
                        print('=' * 30)
                        print('=' * 30)
                        nome = str(input('Digite o nome do produto: '))
                        estoque = int(input('Qual a quantidade: '))
                        preco = float(input('Qual o preço: R$ '))
                        produtos[nome] = [estoque, preco]
                        print(produtos.keys(), produtos.values())
                        print('=' * 30)
                        novo = str(input('Cadastrar novo produto? [S/N]'))
                        if novo in 'Nn':
                            print('.\n.\n.\n')
                            break
                elif num == 2:
                    print('Em construção...')
                elif num == 3:
                    print('Em construção...')
                elif num == 4:
                    print('.\n.\n.\n')
                    break
            elif num1 == 3:
                print('Em construção...')
            elif num1 == 4:
                print('.\n.\n.\n')
                break
    elif num == 2:
        print('Volte Sempre!!!')
        break



