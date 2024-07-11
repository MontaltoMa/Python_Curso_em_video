"""
EXERCÍCIO 022: Analisador de Textos

Crie um programa que leia o nome completo de uma pessoa e mostre:

> O nome com todas as letras maiúsculas e minúsculas.
> Quantas letras ao todo (sem considerar espaços).
> Quantas letras tem o primeiro nome.
"""

nome = input('Digite seu nome completo: \n')
separa =  nome.split()

print('Analisando seu noem...')
print(f'Seu nome com todas as letras maiúsculas {nome.upper()}')
print(f'Seu nome com todas as letras minusculas {nome.lower()}')
print(f'Seu nome tem {len(nome) - nome.count(' ')} letras sem espacos em branco')
print(f'seu primeiro nome tem {len(separa[0])} letras')
print(f'Seu segundo nome tem {len(separa[1])} letras')
print(f'Seu ultimo nome tem {len(separa[2])} letras')