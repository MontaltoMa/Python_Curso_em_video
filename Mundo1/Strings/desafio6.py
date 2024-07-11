"""
EXERCÍCIO 027: Primeiro e Último Nome de uma Pessoa

Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro
e o último nome separadamente.

Ex: Ana Maria de Souza
Primeiro = Ana
Último = Souza
"""

nome = str(input('Digite seu nome completo: \n')).title()

separado = nome.split()

print('Muito prazer em te conhecer!')
print(f'Seu primeiro nome e {separado[0]}')
print(f'Seu ultimo nome e {separado[2]}')