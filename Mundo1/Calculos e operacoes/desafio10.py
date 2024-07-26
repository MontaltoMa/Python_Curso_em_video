# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento

num = float(input('Digite o salario atual do funcionario: \nR$ '))

increase = num * 15 /100

print(f'O salario atural do funcionario e R${num:.2f} com o aumento de 15% foi para R${num + increase:.2f} tendo um aumento de R${increase:.2f}')