# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

n = float(input('DIgite o valor do produto: \n'))

print(f'O valor do prodruto sem desconto e R${n:.2f}')

desc = (n * 5 / 100)

print(f'O valor do produto com 5% de desconto e R${n - desc:.2f}')