'''Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar.
No final, mostre:
a) qual é o total gasto na compra
b) quantos produtos custam mais de R$ 1000
c) qual é o nome do produto mais barato
'''
total = 0
mais_caros = 0
menor_preco = float('inf')
nome_produto= ''

while True:
    produto = str(input('Digite o nome do produto\n'))
    preco = float(input('Digite o valor do produto\nR$'))
    total += preco

    if preco > 1000:
        mais_caros += 1
    
    if preco < menor_preco:
        # Se o preco do produto for menor que menor_preco o nome do produto e salvo em nome_produto
        nome_produto = produto

    continuar = str(input('Deseja continuar? [S/N]')).strip().upper()

    while continuar not in ['S', 'N']:
        continuar = str(input('Digite um dos valores validos [S/N]')).strip().upper()

    if continuar == 'N':
        break

print(f'O total gasto foi R${total:.2f}')
print(f'{mais_caros} Produtos custam mais de R$ 1000')
print(f'O nome do produto mais barato e {nome_produto}')