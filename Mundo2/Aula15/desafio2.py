''' Faça um programa que mostre a tabuada de vários números,
um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo
'''
num = 1

while num >= 1:
    num = int(input('Digite o numero para saber sua tabuada:\n'))

    if num < 1:
        break
    for i in range(1, 11):
        result = num * i
        print(f'{num } * {i} = {result}')