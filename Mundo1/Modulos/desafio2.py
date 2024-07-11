# Desafio 17: Faça um programa que leia o comprimento do cateto oposto (co) e do cateto adjacente (ca) de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

from math import hypot

co = float(input('Digite o comprimento do catoto oposto: \n'))

ca = float(input('Digite o comprimento do cateto adjacente \n'))

hi = hypot(co, ca)

print(f'O comprimento do cateto oposto e {co} e o adjacente {ca}, seu comprimento da hipotenusa e {hi:.2f}')