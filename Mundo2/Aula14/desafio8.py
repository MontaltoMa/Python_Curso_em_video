'''
Crie um programa que leia vários números inteiros pelo teclado
O programa só vai parar quando o usuário digitar o valor 999,
que é a condição de parada

No final, mostre quantos números foram digitados e qual foi a soma
entre eles (desconsiderando o flag!)
'''

cont = 0
res = 0

while True:
    num = int(input('Digite um numero inteiro:\n'))

    if num < 999:
        cont += 1
        res += num
    elif num == 999:
        break
    
print(f'A soma de todos os numeros e: {res}')
print(f'Fora digitados {cont} numeros!')