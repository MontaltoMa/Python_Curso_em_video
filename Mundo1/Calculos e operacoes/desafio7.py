# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar

# Considere R$ 3.27 = US$ 1

num = float(input('Digite seu saldo em carteira: \n'))

dolar = 3.27
conversion = num / dolar

print(f'Seu saldo atual e de {num:.2f}R$ voce pode comprar {conversion:.2f}US$')