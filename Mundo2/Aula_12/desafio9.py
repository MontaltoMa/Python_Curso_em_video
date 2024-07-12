'''
Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal, e condição de pagamento:

- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço normal
- em 3x ou mais no cartão: 20% de juros
'''
produto = float(input('Digite o valor do produto: \nR$'))

forma_de_pagamento = int(input('''Digite a forma de pagamento
1 - Dinheiro ou Cheque
2 - Cartao a vista
3 - Cartao em ate 2X
4 - Cartao em ate 3X \n'''))

dinheiro =  produto - (produto * 0.10)
cartao = produto - (produto * 0.05)
parcelado = produto + (produto * 0.20)

if forma_de_pagamento == 1:
    print('Pagamento em Dinheiro ou Cheque!')
    print(f'O produto custa R${produto}, com o desconto fica R${dinheiro}')
elif forma_de_pagamento == 2:
    print('Pagamento em cartao a vista!')
    print(f'O produto custa R${produto}, com o desconto fica R${cartao}')
elif forma_de_pagamento == 3:
    print('Pagamento em 2X')
    print(f'O produto custa R${produto}, neste caso nao tem desconto nem acrescimo')
elif forma_de_pagamento == 4:
    print('Pagamento parcelado em 3X')
    print(f'O produto custa R${produto}, com o parcelamento fica R${parcelado}')
else:
    print('Digite uma forma de pagamento valida')