'''
Faça um programa que leia o sexo de uma pessoa
mas só aceite os valores "M" ou "F".
Caso esteja errado, peça a digitação novamente
até ter um valor correto.
'''

while True:
    sexo = str(input('Digite seu sexo [M/F]')).strip().upper()

    if sexo not in ['M', 'F']:
        print('Digite um dos dois sexos acima. Digite novamente')
    else:
        print(f'Voce e do sexo: {sexo} !')
        break