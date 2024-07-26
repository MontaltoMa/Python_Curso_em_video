"""
EXERCÍCIO 026: Primeira e Última Ocorrência de uma String

Faça um programa que leia uma frase pelo teclado e mostre:

> Quantas vezes aparece a letra "A".
> Em que posição ela aparece a primeira vez.
> Em que posição ela aparece a última vez.
"""

phrase = input("Digite uma frase: \n").strip().upper()

# Quantidade de vezes que a letra "A" aparece
amount_a = phrase.count('A')

# Posição da primeira ocorrência da letra "A"
first_position = phrase.find('A') + 1

# Posição da última ocorrência da letra "A"
last_position = phrase.rfind('A') + 1

print(f'A frase contém {amount_a} vezes a letra A.')
print(f'A primeira vez que a letra A aparece é na posição {first_position}.')
print(f'A última vez que a letra A aparece é na posição {last_position}.')