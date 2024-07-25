''' Faça um programa que jogue par ou ímpar com o computador.
O jogo só será interrompido quando o jogador perder,
mostrando o total de vitórias consecutivas que ele conquistou, 
no final do jogo.'''

from random import randint

vencedor = False

vitorias = 0

print('=========Bem vindo ao Impar ou Par contra o computador !=========')

while vencedor == False:
    # Jogada da maquina
    jogada_maquina = randint(0, 10)
    # Jogada do player
    escolha = str(input('Voce sera impar ou par?\n')).strip().lower()

    if escolha not in ['impar', 'par']:
        print('Voce digitou algo errado, tente novamente')
    else:

        escolha_jogador = int(input('Digite um numero inteiro positivo:\n'))
        if escolha_jogador < 0:
            print('Erro: O numero digitado e negativo')
        elif escolha_jogador > 10:
            print('Erro: O numero nao pode ser maior que 10')
        else:

            soma = escolha_jogador + jogada_maquina
            resultado = ''

            # Estrutura para saber se o resultado da soma e par ou impar
            if soma % 2 == 0:
                resultado = 'Par'
            elif soma % 2 != 0:
                resultado = 'Impar'

            if soma % 2 == 0 and escolha == 'par':
                print(f'Voce escolheu {escolha_jogador} e a maquina {jogada_maquina} a soma dos dois e {soma} que e {resultado}')
                print('Parabens voce venceu a maquina')
                vitorias += 1
            elif soma % 2 == 0 and escolha == 'impar':
                print(f'Voce escolheu {escolha_jogador} e a maquina {jogada_maquina} a soma dos dois e {soma} que e {resultado}')
                print('A maquina ganhou!')
                vencedor = True
            elif soma % 2 != 0 and escolha == 'par':
                print(f'Voce escolheu {escolha_jogador} e a maquina {jogada_maquina} a soma dos dois e {soma} que e {resultado}')
                print('A maquina ganhou!')
                vencedor = True
            elif soma % 2 != 0 and escolha == 'impar':
                print(f'Voce escolheu {escolha_jogador} e a maquina {jogada_maquina} a soma dos dois e {soma} que e {resultado}')
                print('Parabens voce venceu a maquina')
                vitorias += 1
print(f'Voce ganhor {vitorias} partidas seguidas')