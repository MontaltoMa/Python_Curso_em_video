'''
Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$ 0,50 por Km para viagens de até 200km
e R$ 0,45 para viagens mais longas
'''

distancia = float(input('Digite a distancia em Km da sua viagem:\n'))


if distancia <= 200:
    valor = distancia * 0.50
else:
    valor = distancia * 0.45

print(f'Voce ira viajar {distancia:.0f}Km nesta viagem, sua passagem ficou R${valor:.2f}')