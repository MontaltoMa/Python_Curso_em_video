# Aluguel de carros:

# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado

# Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0.15 por km rodado

CARRO = 'FIAT Palio'

km = float(input('Digite quantos KM percorreu com o carro: \n'))

dias = int(input('Quantos dias ficou com o carro: \n'))

calc_km = km * 0.15

calc_dias = dias * 60

valor_final = calc_km + calc_dias

print(f'Voce alugou com o carro {CARRO} por {dias} dias, percorrendo {km}KM totalizando R${valor_final:.2f}')