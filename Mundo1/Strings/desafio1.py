"""
EXERCÍCIO 022: Analisador de Textos

Crie um programa que leia o nome completo de uma pessoa e mostre:

> O nome com todas as letras maiúsculas e minúsculas.
> Quantas letras ao todo (sem considerar espaços).
> Quantas letras tem o primeiro nome.
"""

name = input('Digite seu nome completo: \n')
separate =  name.split()

print('Analisando seu noem...')
print(f'Seu nome com todas as letras maiúsculas {name.upper()}')
print(f'Seu nome com todas as letras minusculas {name.lower()}')
print(f'Seu nome tem {len(name) - name.count(' ')} letras sem espacos em branco')
print(f'seu primeiro nome tem {len(separate[0])} letras')
print(f'Seu segundo nome tem {len(separate[1])} letras')
print(f'Seu ultimo nome tem {len(separate[2])} letras')