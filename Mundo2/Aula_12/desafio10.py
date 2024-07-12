'''
Crie um programa que faça o computador jogar Jokenpô com você.
'''
from random import choice
from time import sleep

lista = ["pedra", "papel", "tesoura"]

print('''
COMPUTADOR: Vamos jogar Pedra, Papel, Tesoura!
As regras são as seguintes:
- Papel vence Pedra e perde para Tesoura
- Pedra vence Tesoura e perde para Papel
- Tesoura vence Papel e perde para Pedra
''')

nome_jogador = input("Digite seu nome: \n")
jogador = str(input("Você escolhe pedra, papel ou tesoura? \n")).lower()

print("JO")
sleep(0.50)
print("KEN")
sleep(0.5)
print("PÔ!!!")

computador = choice(lista)
vencedor = ' '
print(f'''
Jogador: {jogador}
Computador: {computador}''')

if jogador != 'pedra' and jogador != 'papel' and jogador != 'tesoura':
    print('Escolha entre uma das opcoes validas')
else:
        if jogador == computador:
            print(f'Empate, o jogador escolheu {jogador} e o computador escolheu {computador}') 
            vencedor = ' '
        elif jogador == 'pedra' and computador == 'tesoura':
            vencedor = jogador
            print(f'O {nome_jogador} foi o vencedor escolheu {jogador} e o computador escolheu {computador}') # Pedra x Tesoura: Pedra
        elif jogador == 'tesoura' and computador == 'pedra':
            vencedor = computador
            print(f'O {nome_jogador} foi o vencedor escolheu {jogador} e o computador escolheu {computador}') # Tesoura x Pedra: Pedra
        elif jogador == 'papel' and computador == 'pedra':
            vencedor = jogador
            print(f'O {nome_jogador} foi o vencedor escolheu {jogador} e o computador escolheu {computador}') # Papel x Pedra: Papel
        elif jogador == 'pedra' and computador == ' papel':
            vencedor = computador
            print(f'O {nome_jogador} foi o vencedor escolheu {jogador} e o computador escolheu {computador}') # Pedra x Papel: Papel
        elif jogador == 'tesoura' and computador == 'papel':
            vencedor = jogador
            print(f'O {nome_jogador} foi o vencedor escolheu {jogador} e o computador escolheu {computador}') # Tesoura x Papel: Tesoura
        elif jogador == 'papel' and computador == 'tesoura':
            vencedor = computador
            print(f'O {nome_jogador} foi o vencedor escolheu {jogador} e o computador escolheu {computador}') # Papel x Tesoura: Tesoura