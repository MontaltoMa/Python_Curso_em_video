'''
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento

Para salários superiores a R$ 1.250,00, calcule um aumento de 10%

Para os inferiores ou iguais, o aumento é de R$ 15%.
'''

salario = float(input('Digite seu salario para calcular o aumento:\nR$'))

if salario > 1250:
    aumento = ((salario * 10) / 100) 
else:
    aumento = ((salario * 15) / 100)

novo_salario = salario + aumento

print(f'Seu salario atual e de R${salario:.2f}.\nCom o aumento passou a ser R${novo_salario:.2f}')