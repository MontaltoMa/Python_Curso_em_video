'''
Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
'''

from random import randint

num = randint(0, 1000)

if num % 2 == 0:
    print(f'O numero {num} e PAR')
else:
    print(f'O numero {num} e IMPAR')