''' Faça um programa que leia um número qualquer e mostre
o seu fatorial 

exemplo: 5! = 5 * 4 * 3 * 2 * 1 = 120
'''

num = int(input('Digite um numero inteiro:\n'))
fat = 1
contador = num

print(f'Calculando {num}! =', end=' ')

while contador > 0:
    try:
        print(contador, end=' ')
        fat *= contador
        contador -= 1
        print('x ' if contador > 0 else f' = {fat}', end='')

    except ValueError:
        print('Error: Valor digitado invalido')