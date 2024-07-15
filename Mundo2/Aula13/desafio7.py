''' Faça um programa que leia um número inteiro e diga se ele é ou não
um número primo'''
num = int(input('Digite um numero inteiro: \n'))

primo = True
current  = (num // 2)

for i in range(current, 0, -1):
    if num & i == 0 and i != 0:
        primo = False

if primo:
    print(f'O numero {num} e primo.')
else:
    print(f'O numero {num} nao e primo')