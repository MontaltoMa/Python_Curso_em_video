# Crie um algoritmo que leia um número e mostre o seu dobro, o seu triplo e sua raiz quadrada:

from math import sqrt

n = int(input('Digite um numero inteiro: \n'))

print(f'O dobro do numero e {n * 2}')
print(f'O triplo do numero e {n * 3}')
print(f'A raiz quadrada do numero e {sqrt(n):.2f}')
