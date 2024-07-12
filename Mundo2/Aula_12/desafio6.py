'''
A Confederação Nacional de Natação precisa de um programa que leia
o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

- até 9 anos: mirim
- até 14 anos: infantil
- até 19 anos: júnior
- até 20 anos: sênior
acima de 20: master
'''

from datetime import datetime

def obter_categoria(idade):
    if idade <= 9:
        return f'O atleta tem {idade} anos, e esta na categoria: Mirin!'
    elif idade <= 14:
        return f'O atleta tem {idade} anos, e esta na categoria: Infantil!'
    elif idade <= 19:
        return f'O atleta tem {idade} anos, e esta na categoria: Junior!'
    elif idade <= 20:
        return f'O atleta tem {idade} anos, e esta na categoria: Senior!'
    else:
        return f'O atleta tem {idade} anos, e esta na categoria: Master!'
    

try:
    nascimento = int(input('Digite o ano do seu nascimento:\n'))
    ano_atual = datetime.now().year
    idade = ano_atual - nascimento
    resultado = obter_categoria(idade)
    print(resultado)
except:
    print('Digite um ano de nascimento valido!')