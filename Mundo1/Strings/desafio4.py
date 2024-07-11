"""
EXERCÍCIO 025: Procurando uma String Dentro de Outra

Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
"""

nome = input('Digite seu nome completo \n').strip()

print(f'Seu nome tem Silva?\n{'SILVA' in nome.upper()}')