print('| Boas-vindas à copiadora da Eduarda Amon! |\n')
def escolha_servico(): # Função para solicitar ao usuário o tipo de serviço desejado
    print('------------- Menu de Serviços -------------')
    print('DIG - Digitalização')
    print('ICO - Impressão Colorida')
    print('IPB - Impressão Preto e Branco')
    print('FOT - Fotocópia')

    while True:
        servico = input('Digite o tipo de serviço desejado: ').upper()

        if (servico == 'DIG' or servico == 'ICO' or servico == 'IPB' or servico == 'FOT'):
            if (servico == 'DIG'):
                return 1.10
            if (servico == 'ICO'):
                return 1.00
            if (servico == 'IPB'):
                return 0.40
            if (servico == 'FOT'):
                return 0.20
        else: # Exibe mensagem de erro se a escolha do serviço for inválida
            print('Escolha inválida. Digite novamente.\n')
            continue


def num_pagina(): # Função para calcular o preço com base na quantidade de páginas desejada
    while True:
        try:
            numero_paginas = int(input('Digite a quantidade de páginas desejada: '))

            if (numero_paginas < 20):
                return numero_paginas
            elif (numero_paginas < 200):
                return numero_paginas - (numero_paginas * 15 / 100)
            elif (numero_paginas < 2000):
                return numero_paginas - (numero_paginas * 20 / 100)
            elif (numero_paginas < 20000):
                return numero_paginas - (numero_paginas * 25 / 100)
            else:  # Exibe mensagem de erro se a quantidade de páginas for inválida
                print('Não trabalhamos com essa quantidade de páginas.\nPor favor, digite novamente.\n')
                continue

        except ValueError: # Tratamento de exceções, exibe mensagem de erro se o valor inserido não for numérico
            print('Por favor, insira um valor numérico válido.\n')
            continue


def servico_extra(): # Função para solicitar serviço adicional
    while True:
        try:
            adicional = input('\nDeseja algum serviço adicional? (S/N) ').upper()

            if (adicional == 'S'):
                print('1 - Encadernação Simples   - R$ 15.00')
                print('2 - Encadernação Capa Dura - R$ 40.00')
                print('0 - Não possuo interesse.')
                servico_adc = int(input('>> '))
                if (servico_adc == 1):
                    return 15
                elif (servico_adc == 2):
                    return 40
                elif(servico_adc == 0):
                    return 0
            elif (adicional == 'N'): # Retorna 0 se nenhum serviço adicional for selecionado
                return 0
            else: # Exibe mensagem de erro se a escolha do serviço adicional for inválida
                print('Escolha inválida. Digite novamente.\n')
                continue

        except ValueError:
            print('Por favor, insira um valor numérico válido.')
            continue

# Código Principal
servico = escolha_servico()
num_pagina = num_pagina()
extra = servico_extra()

# Calcula o total a ser pago considerando o serviço, número de páginas e serviço adicional
total = (servico * num_pagina) + extra
print(f'Valor total: R${total:.2f}.')
print(f'(Serviço: {servico:.2f} x Páginas: {num_pagina} + Extra: {extra})')