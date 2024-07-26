''' Escreva um programa que leia a velocidade de um carro
Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado
A multa vai custar R$7,00 por cada Km acima do limite.
'''

from random import randint
from time import sleep

#Usei o randint para criar situacoes diversas
speed = randint(20, 200)

#Calcula a multa pegando a velocidade do carro e subtraindo pelo limite da via para saber quanto sera a multa final
t_ticket = (speed - 80) * 7 

if speed > 80:
    print(f'Voce estava a {speed}KM em uma via de 80KM')
    print('Voce foi multado estamos calculando o valor da multa!')
    sleep(1)
    print(f'Valor a pagar R${t_ticket:.2f}')
else:
    print(f'Voce estava a {speed}KM na via onde o limite era 80KM, continue dirigindo com cuidado!')