# Crie um algoritmo que leia um número e mostre o seu dobro, o seu triplo e sua raiz quadrada:

from math import sqrt

num = int(input('Digite um numero inteiro: \n'))

print(f'O dobro do numero e {num * 2}')
print(f'O triplo do numero e {num * 3}')
print(f'A raiz quadrada do numero e {sqrt(num):.2f}')
