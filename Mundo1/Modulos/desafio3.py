# Desafio 18: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import cos, sin, tan, radians

num = float(input('Digite um ângulo de uma circunferência (ou seja, entre 0º e 360º): \n \n'))

# Calcula e exibe o seno, cosseno e tangente do ângulo
print(f'O valor do Seno: {sin(radians(num)):.2f}')
print(f'O valor do cosseno: {cos(radians(num)):.2f}')
print(f'O valor da tangente: {tan(radians(num)):.2f}')
