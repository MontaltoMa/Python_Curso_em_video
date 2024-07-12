'''

Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC
e mostre seu status, e acordo com a tabela abaixo:

- abaixo de 18.5: abaixo do peso
- entre 18.5 e 25: peso ideal
- 25 até 30: sobrepeso
- 30 até 40: obesidade
- acima de 40: obesidade mórbida
'''

peso = float(input('Digite seu peso em Kg: '))
altura = float(input('Digite sua altura em metros: '))

if altura == 0:
    print('Erro, altura não pode ser zero.')
else:
    imc = (peso / (altura ** 2))
    if imc <= 18.5:
        print(f'Seu imc é {imc:.2f}, você está abaixo do peso ideal. ')
    elif imc <= 25:
        print(f'Seu imc é {imc:.2f}, você está no peso ideal.')
    elif imc <= 30:
        print(f'Seu imc é {imc:.2f}, você está acima do peso.')
    elif imc <= 35:
        print(f'Seu imc é {imc:.2f}, você está com obesidade grau 1.')
    elif imc <= 40:
        print(f'Seu imc é {imc:.2f}, você esta com obesidade grau 2 (severa).')
    else:
        print(f'Seu imc é {imc:.2f}, você esta com obesidade grau 3 (mórbida).')