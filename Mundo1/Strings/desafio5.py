"""
EXERCÍCIO 026: Primeira e Última Ocorrência de uma String

Faça um programa que leia uma frase pelo teclado e mostre:

> Quantas vezes aparece a letra "A".
> Em que posição ela aparece a primeira vez.
> Em que posição ela aparece a última vez.
"""

frase = input("Digite uma frase: \n").strip().upper()

# Quantidade de vezes que a letra "A" aparece
quantidade_a = frase.count('A')

# Posição da primeira ocorrência da letra "A"
primeira_posicao = frase.find('A') + 1

# Posição da última ocorrência da letra "A"
ultima_posicao = frase.rfind('A') + 1

print(f'A frase contém {quantidade_a} vezes a letra A.')
print(f'A primeira vez que a letra A aparece é na posição {primeira_posicao}.')
print(f'A última vez que a letra A aparece é na posição {ultima_posicao}.')