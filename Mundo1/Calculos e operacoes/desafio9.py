# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

num = float(input('DIgite o valor do produto: \n'))

print(f'O valor do prodruto sem desconto e R${num:.2f}')

desc = (num * 5 / 100)

print(f'O valor do produto com 5% de desconto e R${num - desc:.2f}')