'''
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento

Para salários superiores a R$ 1.250,00, calcule um aumento de 10%

Para os inferiores ou iguais, o aumento é de R$ 15%.
'''

salari = float(input('Digite seu salario para calcular o aumento:\nR$'))

if salari > 1250:
    increase = ((salari * 10) / 100) 
else:
    increase = ((salari * 15) / 100)

new_salario = salari + increase

print(f'Seu salario atual e de R${salari:.2f}.\nCom o aumento passou a ser R${new_salario:.2f}')