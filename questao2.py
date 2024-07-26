print('| Boas-vindas à loja de Gelados da Eduarda Amon! |')
print('-' * 20, 'Cardápio', '-' * 20)
print('-' * 50)
print('---|  Tamanho  |  Cupuaçu (CP)  |  Açaí (AC)  |---')
print('---|     P     |    R$  9.00    |   R$ 11.00  |---')
print('---|     M     |    R$ 14.00    |   R$ 16.00  |---')
print('---|     G     |    R$ 18.00    |   R$ 20.00  |---')
print('-' * 50)

valor_total = 0  # Inicializa o valor total do pedido

# Loop principal para receber os pedidos do usuário
while True:
    # Solicita ao usuário o sabor desejado e verifica se é válido
    sabor = input('Digite o sabor desejado (CP/AC): ').upper()
    if (sabor != 'AC' and sabor != 'CP'):
        print('Sabor inválido. Tente novamente.\n')
        continue

    # Solicita ao usuário o tamanho desejado e verifica se é válido
    tamanho = input('Digite o tamanho desejado (P/M/G): ').upper()
    if (tamanho != 'P' and tamanho != 'M' and tamanho != 'G'):
        print('Tamanho inválido. Tente novamente.\n')
        continue

    preco = 0  # Inicializa o preço do pedido

    # Calcula o preço com base no sabor e tamanho selecionados
    if (sabor == 'CP'):
        if (tamanho == 'P'):
            preco = 9.00
            valor_total += preco  # Adiciona o preço do pedido ao valor total
            print(f'Você pediu um Cupuaçu no tamanho P: R${preco}\n')
        elif (tamanho == 'M'):
            preco = 14.00
            valor_total += preco
            print(f'Você pediu um Cupuaçu no tamanho M: R${preco}\n')
        elif (tamanho == 'G'):
            preco = 18.00
            valor_total += preco
            print(f'Você pediu um Cupuaçu no tamanho G: R${preco}\n')
    elif (sabor == 'AC'):
        if (tamanho == 'P'):
            preco = 11.00
            valor_total += preco
            print(f'Você pediu um Açaí no tamanho P: R${preco}\n')
        elif (tamanho == 'M'):
            preco = 16.0
            valor_total += preco
            print(f'Você pediu um Açaí no tamanho M: R${preco}\n')
        elif (tamanho == 'G'):
            preco = 20.0
            valor_total += preco
            print(f'Você pediu um Açaí no tamanho G: R${preco}\n')

    # Pergunta se o usuário deseja pedir mais alguma coisa, se sim, continua o loop
    pedido = input('Deseja pedir mais alguma coisa? (S/N) ').upper()
    if (pedido == 'S'):
        continue
    else:
        print('Encerrando pedido...')
        break

print(f'\nO valor total a ser pago: R${valor_total}')  # Exibe o valor total