# Importação da função time da biblioteca para criar tempo de espera
from time import sleep

# Importação de os para aplicar a função limpar telar
import os
def LimpaTela():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')




# Tela inicial - Menu Boas vindas

while True:
    LimpaTela()
    print('*' * 64)
    print('*' * 64)
    print(f'{"Seja bem vindo ao Organico’s 🙂.":^60}\n{"Aqui você pode comprar nossos produtos direto pelo seu celular!":^60}')
    print('*' * 64)
    print('*' * 64)
    print('Para entrar no programa digite [1] \nPara sair do programa digite [2]')
    num = input("Digite o que deseja: ")
    while num not in '12' or 0 > len(num) or len(num) > 1:
        num = input('Código inválido! Digite novamente: ')
    if num == '1':
        print('Que bom que está continuando com a gente!\nVocê está sendo redirecionada(o) para o nosso menu de navegação! Aguarde...')
        sleep(3)

        # Menu de Navegação
        while True:
            LimpaTela()
            print('*' * 64)
            print('*' * 64)
            print(f'{"Seja bem vindo ao menu de navegação!":^64}')
            print('*' * 64)
            print('*' * 64)
            num = input('[1] Menu de Cadastro;\n[2] Menu de Vendas;\n[3] Voltar.\nDigite o número de uma das opções acima:  ')
            while num not in '1234' or len(num) > 1 or len(num) < 0:
                num = input('Por favor, digite o valor 1, 2 ou 3. \nDigite o que deseja: ')
            print('Processando...')
            sleep(3)
            if num == '1':

                # Menu de cadastro de produtos
                produto = []
                lista_cadastrados = []
                while True:
                    LimpaTela()
                    print('*' * 64)
                    print('*' * 64)
                    print(f'{"Olá! Agora que estamos no menu de cadastro, ":^64}\n{"digite o número de uma das opções abaixo":^64}\n{"para ser redirecionado novamente: ":^64}')
                    print('*' * 64)
                    print('*' * 64)
                    num = input("[1] Cadastrar produto;\n[2] Listar produtos cadastrados;\n[3] Deleção de produtos;\n[4] Voltar\nDigite o que deseja: ")
                    if num == '1':

                        # Inclusão de produto(nome e preço)
                        print('Acessando cadastro de produtos...')
                        sleep(3)
                        while True:
                            LimpaTela()

                            # Adição do nome
                            while True:
                                print('Vamos cadastrar o produto...\n')
                                nome = input('Digite o nome do produto: ').capitalize()

                                # Verificação se o nome contém apenas letras
                                if nome.isalpha() == True:

                                    # Verificação se produto já está cadastrado
                                    if len(lista_cadastrados) > 0:
                                        cont_nome_existente = 0
                                        for z in range(0, len(lista_cadastrados)):
                                            if lista_cadastrados[z][0] == nome:
                                                cont_nome_existente += 1
                                        if cont_nome_existente > 0:
                                            print('Produto já cadastrado! Tente novamente!')
                                        else:
                                            break
                                    else:
                                        break

                                else:
                                    print('Nome inválido! O nome pode conter apenas letras.')

                            # Inclusão do preço
                            while True:
                                preco = input('Qual o preço: R$ ').replace(',', '.')

                                #Verificação se a string recebida pode ser transformada em float
                                validador = 0
                                for i, v in enumerate(preco):
                                    if preco[i] in "0123456789.":
                                        validador += 1
                                if validador == len(preco):
                                    preco = float(preco)
                                    break
                                else:
                                    print('Preço inválido! Digite apenas números.')

                            # Nome e preço adicionados na lista produtos
                            produto.append(nome)
                            produto.append(preco)
                            print(f'\nParabéns!!!\nO produto [{nome}] com o preço [R$ {preco:.2f}] foi cadastrado com sucesso!')

                            # A cópia da lista produtos adicionado a lista_cadastrados
                            lista_cadastrados.append(produto[:])

                            # Cadastradar ou não novo produto e reiniciar/brekar o looping
                            novo = str(input('Cadastrar novo produto? [S/N] '))[0]
                            while novo not in "SsNn":
                                print('Código inválido!')
                                novo = str(input('Digite [S] p/ sim ou [N] p/ não: '))[0]
                            produto.clear()
                            if novo in 'Nn':
                                break

                    elif num == '2':

                        # Menu listar produtos
                        while True:
                            LimpaTela()
                            print('Buscando lista de produtos cadastrados, por favor, aguarde...\n')
                            sleep(3)

                            # Se lista não está vazia
                            if len(lista_cadastrados) > 0:
                                print('*'*45)
                                print(f'{"Código":<10}{"Nome do Produto":<20}{"Preço":>10}')
                                print('*'*45)

                                #cont_01 é um contador
                                cont_01 = 0
                                while cont_01 < len(lista_cadastrados):
                                    print(f'{cont_01:^10}{lista_cadastrados[cont_01][0]:.<20}R${lista_cadastrados[cont_01][1]:.>10.2f}')
                                    cont_01 += 1

                            # Se lista está vazia
                            else:
                                print('*'*45)
                                print('Nenhum produto cadastrado!')
                                print('*'*45)

                            # Opção de mostrar a lista novamente
                            pergunta = input('\nMostrar lista novamente? [S/N] ').strip().capitalize()[0]
                            while pergunta not in "SsNn":
                                print('Código inválido!')
                                pergunta = input('Digite [S] p/ sim ou [N] p/ não: ')
                            if pergunta in 'Ss':
                                print()
                            elif pergunta in 'Nn':
                                break

                    elif num == '3':

                        # Menu para deletar produtos da lista de cadastros
                        while True:
                            LimpaTela()
                            print('\nATENÇÃO! Aqui você poderá deletar produtos...')
                            sleep(2)
                            print('\nInicialmente, veja a lista de produtos cadastrados...\n')
                            sleep(2)

                            # Lista os produtos para vincular o código do produto ao índice da lista
                            if len(lista_cadastrados) > 0:
                                print('*' * 45)
                                print(f'{"Código":<10}{"Nome do Produto":<20}{"Preço":>10}')
                                print('*' * 45)
                                cont_01 = 0
                                while cont_01 < len(lista_cadastrados):
                                    print(f'{cont_01:^10}{lista_cadastrados[cont_01][0]:.<20}R${lista_cadastrados[cont_01][1]:.>10.2f}')
                                    cont_01 += 1

                                # Opção para deletar
                                deletar = str(input('\nQuer deletar algum produto? [S/N] ')).strip()[0]
                                while deletar not in "SsNn":
                                    print('Código inválido!')
                                    deletar = str(input('Digite [S] p/ sim ou [N] p/ não: '))
                                if deletar in "Ss:":
                                    num_del = int(input('\nDigite o código do produto a ser deletado: '))
                                    while True:
                                        if 0 <= num_del <= len(lista_cadastrados) - 1:
                                            print(f'O Produto [{lista_cadastrados[num_del][0]}] foi deletado com sucesso!')
                                            del lista_cadastrados[num_del]
                                            break
                                        else:
                                            print('Código de produto inválido!')
                                            num_del = int(input('Digite o código do produto a ser deletado: '))
                                else:
                                    break
                            else:
                                print('Nenhum produto cadastrado!')

                            # Questionamento para continuar deleção ou sair
                            num = input('O que deseja fazer agora?\n[1] Deletar outro produto;\n[2] Voltar;\nDigite a opção: ')
                            while num not in "12" or num < 1 or num > 2:
                                print('Código inválido!')
                                num = input('Digite a opção: ')
                            if num == '1':
                                print()
                            elif num == '2':
                                break

                    # Interrompe o looping do menu cadastro
                    elif num == '4':
                        break

            elif num == '2':

                # Menu de vendas
                carrinho = []
                while True:
                    LimpaTela()
                    print('*' * 64)
                    print('*' * 64)
                    print(
                        f'{"Olá! Agora que estamos no menu de vendas, ":^64}\n{"digite o número de uma das opções abaixo":^64}\n{"para ser redirecionado novamente: ":^64}')
                    print('*' * 64)
                    print('*' * 64)
                    num = input("[1] Listar produtos no carrinho;\n[2] Adicionar produtos ao carrinho;\n[3] Excluir produtos do carrinho;\n[4] Finalizar compra;\n[5] Voltar;\nDigite o que deseja: ")
                    while num not in '12345' or 0 > len(num) or len(num) > 1:
                        num = input('Código inválido! Digite novamente: ')

                    if num == '1':

                        # Menu listar produtos do carrinho
                        while True:
                            LimpaTela()
                            print('\nAcessando produtos já incluídos no carrinho...\n')
                            sleep(2)
                            # Se carrinho não está vazio
                            if len(carrinho) > 0:
                                print('*' * 45)
                                print(f'{"Código":<10}{"Nome do Produto":<20}{"Preço":>10}')
                                print('*' * 45)

                                # cont_01 é um contador
                                cont_01 = 0
                                while cont_01 < len(carrinho):
                                    print(
                                        f'{cont_01:^10}{carrinho[cont_01][0]:.<20}R${carrinho[cont_01][1]:.>10.2f}')
                                    cont_01 += 1

                            # Se carrinho está vazio
                            else:
                                print('*' * 45)
                                print('Nenhum produto encontrado!')
                                print('*' * 45)

                            # Opção de mostrar conteúdo do carrinho novamente
                            pergunta = input('\nMostrar conteúdo do carrinho novamente? [S/N] ').strip().capitalize()
                            while pergunta not in "SsNn":
                                print('Código inválido!')
                                pergunta = input('Digite apenas [S] p/ sim ou [N] p/ não: ')
                            if pergunta in 'Ss':
                                # Print apenas para não deixar conteúdo do if vazio
                                print()
                            elif pergunta in 'Nn':
                                break

                    elif num == '2':

                        # Menu para adicionar produtos ao carrinho
                        while True:
                            LimpaTela()
                            print('\nAqui você poderá adicionar produtos no carrinho...')
                            sleep(2)
                            print('\nInicialmente, veja a lista de produtos cadastrados...\n')
                            sleep(2)

                            # Lista os produtos para vincular o código do produto ao índice da lista
                            if len(lista_cadastrados) > 0:
                                print('*' * 45)
                                print(f'{"Código":<10}{"Nome do Produto":<20}{"Preço":>10}')
                                print('*' * 45)
                                cont_01 = 0
                                while cont_01 < len(lista_cadastrados):
                                    print(f'{cont_01:^10}{lista_cadastrados[cont_01][0]:.<20}R${lista_cadastrados[cont_01][1]:.>10.2f}')
                                    cont_01 += 1

                                while True:
                                    cod_produto = input('\nDigite o código do produto a ser adicionado: ')
                                    if cod_produto.isdigit() != True or len(cod_produto) > 1 or len(cod_produto) < 1:
                                        print('Código de produto inválido!')
                                    else:
                                        cod_produto = int(cod_produto)
                                        if 0 <= cod_produto <= len(lista_cadastrados) - 1:
                                            print(f'O Produto [{lista_cadastrados[cod_produto][0]}] foi adicionado com sucesso!')
                                            carrinho.append(lista_cadastrados[cod_produto][:])
                                            break
                                        else:
                                            print('Código de produto inválido!')


                                # Questionamento para continuar adicionando ou sair
                                num = input('O que deseja fazer agora?\n[1] Adicionar outro produto ao carrinho;\n[2] Voltar;\nDigite a opção: ')
                                while num not in "12" or len(num) != 1:
                                    print('Código inválido!')
                                    num = input('Digite a opção: ')
                                if num == '1':
                                    print()
                                elif num == '2':
                                    break

                            # Caso não exista produtos na lista para comprar
                            else:
                                print('Ainda não existem produtos disponíveis para compra!')
                                print('Contate o fornecedor para atualização do cadastro de produtos.')
                                sleep(6)
                                print('Voltando para o menu anterior...')
                                sleep(3)
                                break

                    elif num == '3':

                        # Menu para deletar produtos do carrinho
                        while True:
                            LimpaTela()
                            print('\nATENÇÃO! Aqui você poderá deletar produtos existentes no carrinho...')
                            sleep(2)
                            print('\nVeja a lista de produtos que seu carrinho possui...\n')
                            sleep(2)

                            # Lista os produtos para vincular o código do produto ao índice da lista
                            if len(carrinho) > 0:
                                print('*' * 45)
                                print(f'{"Código":<10}{"Nome do Produto":<20}{"Preço":>10}')
                                print('*' * 45)
                                cont_01 = 0
                                while cont_01 < len(carrinho):
                                    print(
                                        f'{cont_01:^10}{carrinho[cont_01][0]:.<20}R${carrinho[cont_01][1]:.>10.2f}')
                                    cont_01 += 1

                                # Opção para deletar
                                deletar = str(input('\nQuer deletar algum produto? [S/N] ')).strip()[0]
                                while deletar not in "SsNn":
                                    print('Código inválido!')
                                    deletar = str(input('\nQuer deletar algum produto? [S/N] ')).strip()[0]
                                if deletar in "Ss":
                                    while True:
                                        cod_produto = input('\nDigite o código do produto a ser deletado: ')
                                        if cod_produto.isdigit() != True or len(cod_produto) > 1 or len(cod_produto) < 1:
                                            print('Código de produto inválido!')
                                        else:
                                            cod_produto = int(cod_produto)
                                            if 0 <= cod_produto <= len(carrinho) - 1:
                                                print(f'O Produto [{carrinho[cod_produto][0]}] foi removido do carrinho com sucesso!')
                                                del carrinho[cod_produto]
                                                break
                                            else:
                                                print('Código de produto inválido!')

                            # Quando carrinho não possui produtos
                            else:
                                print('Não é possivel excluir produtos - não há itens no carrinho.')
                                sleep(6)
                                print('Voltando para o menu anterior...')
                                sleep(3)
                                break


                            # Questionamento para continuar deleção ou sair
                            num = input('O que deseja fazer agora?\n[1] Deletar outro produto;\n[2] Voltar;\nDigite a opção: ')
                            while num not in "12" or len(num) != 1:
                                print('Código inválido!')
                                num = input('Digite a opção: ')
                            if num == '1':
                                print()
                            elif num == '2':
                                break

                    elif num == '4':

                        # Menu finalizar compras do carrinho
                        while True:
                            LimpaTela()
                            print('\nAcessando produtos já incluídos no carrinho...\n')
                            sleep(2)

                            # Se carrinho não está vazio
                            if len(carrinho) > 0:
                                print('*' * 45)
                                print(f'{"Lista de compras":^40}')
                                print(f'{"Nome do Produto":<20}-->{"Preço":>10}')
                                print('*' * 45)

                                # cont_01 é um contador
                                cont_01 = 0
                                while cont_01 < len(carrinho):
                                    print(f'{carrinho[cont_01][0]:.<20}R${carrinho[cont_01][1]:.>12.2f}')
                                    cont_01 += 1
                                soma = 0
                                for c in range(0, len(carrinho)):
                                    soma = soma + carrinho[c][1]
                                print('*' * 45)
                                print(f'{"Total":.<20}R${soma:.>12.2f}')
                                print('*' * 45)

                                # Opção para finalizar compra e limpar carrinho
                                final = input('Deseja finalizar a compra? [S ou N]').strip()[0]
                                while final not in "SsNn":
                                    print('Código inválido!')
                                    final = str(input('\nDeseja finalizar a compra? [S ou N] ')).strip()[0]
                                if final in "Ss":
                                    print('Compra finalizada!\nCarrinho esvaziado.')
                                    carrinho.clear()
                                    print('Voltando para o menu anterior...')
                                    sleep(6)
                                    break
                                else:
                                    print('Voltando para o menu anterior...')
                                    sleep(6)
                                    break

                            # Se carrinho está vazio
                            else:
                                print('*' * 45)
                                print('Nenhum produto encontrado!')
                                print('*' * 45)
                                input('Para voltar para ao menu anterior pressione [enter].')
                                break



                    elif num == '5':
                        break

            elif num == '3':
                # Voltar para menu inicial
                break

    # Encerrar o programa
    elif num == '2':
        print('Obrigada por visitar nosso programa. Volte sempre!')
        sleep(4)
        break



