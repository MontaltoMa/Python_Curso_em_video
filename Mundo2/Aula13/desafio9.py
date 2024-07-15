''' Crie um programa que leia o ano de nascimento de sete pessoas
No final, mostre quantas pessoas ainda não atingiram a maioridade
e quantas já são maiores'''

from datetime import datetime

ano_atual = datetime.now().year
menor = 0
maior = 0
for i in range(7):
    ano = int(input('Digite o ano do seu nascimento: \n'))
    result = ano_atual - ano
    if result < 18:
        menor += 1
    else:
        maior += 1
print(f'No total {menor} pessoas ainda nao sao maiores de idade, e {maior} sao maiores de idade')