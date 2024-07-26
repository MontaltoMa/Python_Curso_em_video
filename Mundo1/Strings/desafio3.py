"""
EXERCÍCIO 024: Verificando as Primeiras Letras de um Texto

Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".
"""
name = input('Digite o nome da sua cidade:\n').strip().upper()

print(f'O nome da sua cidade comeca com Santa? {name[:5] == 'SANTO'}')