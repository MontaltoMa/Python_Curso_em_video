# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento

n = float(input('Digite o salario atual do funcionario: \nR$ '))

aumento = n * 15 /100

print(f'O salario atural do funcionario e R${n:.2f} com o aumento de 15% foi para R${n + aumento:.2f} tendo um aumento de R${aumento:.2f}')