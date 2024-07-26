print('| Boas-vindas à loja da Eduarda Amon! |')

valor = int(input('Insira o valor unitário do produto: '))
qtd = int(input('Insira a quantidade do produto: '))

# Calcula o valor total dos produtos sem desconto
valor_total = valor * qtd

# Determina o desconto com base no valor unitário do produto
if (valor_total < 2500):
  desconto = 0
elif (valor_total < 6000):
  desconto = valor_total * 4 / 100
elif (valor_total < 10000):
  desconto = valor_total * 7 / 100
else:
  desconto = valor_total * 11 / 100

# Calcula o valor total dos produtos com desconto
valor_desconto = valor_total - desconto

print(f'Valor total: {valor_total}')
print(f'Valor com desconto: {valor_desconto}')