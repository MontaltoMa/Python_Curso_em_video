''' Refaça o desafio 009, mostrando a tabuada de um número
que o usuário escolher, só que agora utilizando um laço for'''

numero = int(input('Digite um numero inteiro para vermos sua tabuada:\n'))

for i in range(1, 11):
    result = numero * i
    print(f'{numero} * {i} = {result}')