print('| Boas-vindas à livraria da Eduarda Amon! |')

# Lista para armazenar os livros e variável para o ID global
lista_livro = []
id_global = 0

def cadastrar_livro(id):  # Função para realizar cadastro de livros
    global id_global
    id_global += 1

    print(f'Id do Livro: {id}') # Mostra o ID do livro ao usuário
    nome = input('Insira o nome do livro: ')
    autor = input('Insira o nome do autor: ')
    editora = input('Insira o nome da editora: ')

    # Cria um dicionário com os detalhes do livro e o adiciona à lista de livros
    livro = {'id': id, 'nome': nome, 'autor': autor, 'editora': editora}
    lista_livro.append(livro)

def consultar_livro(): # Função para consultar os livros
    while True:
        print()
        print('----- Menu de Opções -----')
        print('1 - Consultar Todos')
        print('2 - Consultar por Id')
        print('3 - Consultar por Autor')
        print('4 - Retornar ao menu')
        try:
            opcao = int(input('Escolha a opção desejada: '))
            print()
            if (opcao == 1):
                for livro in lista_livro:  # Mostra todos os livros cadastrados
                    print(f'Id: {livro["id"]}')
                    print(f'Nome: {livro["nome"]}')
                    print(f'Autor: {livro["autor"]}')
                    print(f'Editora: {livro["editora"]}\n')

            elif (opcao == 2): # Consulta um livro pelo ID
                consulta_id = int(input('Insira o de Id do livro desejado: '))
                livro_encontrado = False
                for livro in lista_livro:
                    if (livro['id'] == consulta_id):
                        print(f'Id: {livro["id"]}')
                        print(f'Nome: {livro["nome"]}')
                        print(f'Autor: {livro["autor"]}')
                        print(f'Editora: {livro["editora"]}\n')
                        livro_encontrado = True
                        break
                if not livro_encontrado:
                    print('Livro não encontrado.')

            elif (opcao == 3): # Consulta livros pelo autor
                consulta_autor = input('Insira o nome do Autor: ')
                livros_encontrados = False
                for livro in lista_livro:
                    if (livro['autor'] == consulta_autor):
                        print(f'Id: {livro["id"]}')
                        print(f'Nome: {livro["nome"]}')
                        print(f'Autor: {livro["autor"]}')
                        print(f'Editora: {livro["editora"]}\n')
                        livros_encontrados = True
                if not livros_encontrados:
                    print('Nenhum livro encontrado para o autor informado.')

            elif (opcao == 4): # Retorna ao menu principal
                break
            else:
                print('Opção inválida. Tente novamente.')
                continue
        except ValueError: # Trata exceção se usuário inserir valor não numérico
            print('Por favor, insira um valor numérico válido.')
            continue

def remover_livro(): # Função para remover um livro
    while True:
        try:
            remover_id = int(input('Insira o Id do livro a ser removido: '))
            if (remover_id == 0):  # Se usuário inserir 0, retorna ao menu principal
                break
            livro_removido = False
            for livro in lista_livro:
                if (livro['id'] == remover_id):
                    lista_livro.remove(livro) # Remove o livro da lista se o ID corresponder
                    print('O livro foi removido.')
                    livro_removido = True
                    break
            if not livro_removido: # Se o ID não corresponder, solicita que o usuário insira novamente
                print('Id inválido. Tente novamente.')
            else:
                return
        except ValueError:  # Trata exceção se usuário inserir valor não numérico
            print('Por favor, insira um valor numérico válido.')
            continue

# Código Principal
while True:
    try:
        print()
        print('----- Menu Principal -----')
        print('1 - Cadastrar Livro')
        print('2 - Consultar Livro')
        print('3 - Remover Livro')
        print('4 - Encerrar Programa')
        opcao = int(input('Escolha a opção desejada: '))

        if (opcao == 1):
            cadastrar_livro(id_global + 1)  # Chama função para cadastrar um livro
        elif (opcao == 2):
            consultar_livro() # Chama função para consultar os livros
        elif (opcao == 3):
            remover_livro()  # Chama função para remover um livro
        elif (opcao == 4):
            print('Encerrando programa...')  # Encerra o programa
            break
        else: # Opção inválida, solicita que o usuário escolha novamente
            print('Opção inválida. Tente novamente.')
            continue
    except ValueError:  # Trata exceção se usuário inserir valor não numérico
        print('Por favor, insira um valor numérico válido.')
        continue