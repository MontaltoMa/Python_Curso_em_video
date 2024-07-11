# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar

# Considere R$ 3.27 = US$ 1

n = float(input('Digite seu saldo em carteira: \n'))

dolar = 3.27
convercao = n / dolar

print(f'Seu saldo atual e de {n:.2f}R$ voce pode comprar {convercao:.2f}US$')