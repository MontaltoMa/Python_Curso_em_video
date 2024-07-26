'''
Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$ 0,50 por Km para viagens de até 200km
e R$ 0,45 para viagens mais longas
'''

distance = float(input('Digite a distancia em Km da sua viagem:\n'))


if distance <= 200:
    value = distance * 0.50
else:
    value = distance * 0.45

print(f'Voce ira viajar {distance:.0f}Km nesta viagem, sua passagem ficou R${value:.2f}')