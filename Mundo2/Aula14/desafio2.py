''' Melhore o jogo do DESAFIO 028 onde o computador vai "pensar"
em um número entre 0 e 10. 
Só que agora o jogador vai tentar adivinhar até acertar, 
mostrando no final quantos palpites foram necessários para vencer
'''
from random import randint

cont = 1
num = randint(0,10)
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
print('-=-' * 20)

while True:

    try:
        escolha =  int(input('Digite um numero entre 0 e 10:\n'))

        if 0 < escolha > 10:
            print('O numero nao pode ser negativo ou maior que 10!')
        elif escolha == num:
            print(f'Parabens voce acertou o numero {num} em {cont} tentativas!')
            break
        elif escolha < num:
            print('Tente um numero maior\n')
            cont += 1
        elif escolha > num:
            print('Tente um numero menor\n')
            cont += 1

    except ValueError:
        print('Entrada inválida. Por favor, digite um número inteiro entre 0 e 10.')