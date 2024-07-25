''' Crie um programa que leia vários números inteiros pelo teclado
O programa só vai parar quando o usuário digitar 999,
que é a condição de parada (flag).
No final, mostre quantos números foram digitados
e qual foi a acc entre eles (desconsiderando o flag)
'''

soma = contador = 0

while True:
    n = int(input('Digite um numero:'))
    if n == 999:
        break
    elif n < 0:
        print('O numero nao pode ser negativo')

    contador+=1
    soma += n
print(f'Foram digitados {contador} numeros!')
print(f'A soma dos numeros e {soma}')