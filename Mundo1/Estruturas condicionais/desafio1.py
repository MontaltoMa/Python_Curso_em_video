'''
Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.

O programa deverá escrever na tela se o usuário venceu ou perdeu.

'''
from random import randint
import time

num = randint(0,5)
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)

choice = int(input('Digite um numero de 0 a 5 para tentar acertar a escolha da maquina: \n'))
print('PROCESSANDO...')
time.sleep(1)
if choice < 0 or choice > 5:
    print('O numero nao pode ser negativo\n')
    print('Dica: O numero precisa estar no intervalo entre 0 e 5')
else:
    if choice == num:
        print(f'O numero escolhido pela maquina foi {num}, parabens voce acertou!')
    else:
        print(f'O numero escolhido era {num}, infelizmente voce errou!')

