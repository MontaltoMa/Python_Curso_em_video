'''
Faça um programa que leia o ano de nascimento de um jovem e informe
de acordo com sua idade:

- Se ele ainda vai se alistar ao serviço militar
- Se é a hora de se alistar
- Se já passou do tempo do alistamento

Seu programa também deverá mostrar o tempo que faltou ou que passou do prazo
'''

from datetime import datetime

print('Voce ainda precisa se alistar?')
ano = int(input('Digite o ano do seu nascimento:\n'))
ano_atual = datetime.now().year
idade = ano_atual - ano


def precisa_se_alistar(idade):
    if idade < 18:
        tempo_para_alistar = ano_atual - ano
        return f'Voce tem {idade} anos ainda vai ter que se alistar daqui {tempo_para_alistar} anos'
    elif idade == 18:
        return f'E hora de se alistar, voce ja tem {idade} anos'
    else:
        passou_do_tempo = idade - 18 
        return f'Ja passou do tempo do alistamento, voce tem {idade} anos e deveria ter se alistado a {passou_do_tempo} anos'
    
resultado = precisa_se_alistar(idade)

print(resultado)