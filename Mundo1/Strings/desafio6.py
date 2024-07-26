"""
EXERCÍCIO 027: Primeiro e Último Nome de uma Pessoa

Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro
e o último nome separadamente.

Ex: Ana Maria de Souza
Primeiro = Ana
Último = Souza
"""

name = str(input('Digite seu nome completo: \n')).title()

separete = name.split()

print('Muito prazer em te conhecer!')
print(f'Seu primeiro nome e {separete[0]}')
print(f'Seu ultimo nome e {separete[2]}')