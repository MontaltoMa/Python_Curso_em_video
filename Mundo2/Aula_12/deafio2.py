''' Escreva um programa que leia um número inteiro qualquer
e peça para o usuário escolher qual será a base de conversão:
1 para binário
2 para octal
2 para hexadecimal
'''

num = int(input('Digite um numero inteiro positivo: \n'))
base = int(input('''Escolha a base da conversão:
Para binário digite: 1
Para octal digite: 2
Para hexadecimal digite: 3

Sua escolha: \n'''))

if base == 1:
    print(f'Voce escolheu {base}')
    print(f'O numero {num} convertido para binário: {num:b}')
elif base == 2:
    print(f'Voice escolheu {base}')
    print(f'O numero {num} convertido para octal: {num:o}')
elif base == 3:
    print(f'Voice escoleu  {base}')
    print(f'O numero {num} convertido para hexadecimal: {num:h}')
else:
    print('Voce escolheu um numero diferente de 1 a 3')