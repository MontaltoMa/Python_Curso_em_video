# Desafio 16: Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.

from math import trunc

num = float(input('Digite um numero real: \n'))

print(f'O numero real digitado foi {num:.2f} e sua portcao inteira e {trunc(num)}')