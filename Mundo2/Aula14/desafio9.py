''' Crie um programa que leia vários números inteiros pelo teclado
No final da execução, mostre a média entre todos os valores
e qual foi o maior e o menor valores lidos
O programa deve perguntar ao usuário se ele quer ou não continuar
a digitar valores
'''

maior = None
menor = None
cont = 0
soma = 0

while True:

    num = int(input('Digite um número inteiro:\n'))
    soma += num
    cont += 1

    # Atualizar maior e menor
    if maior is None or num > maior:
        maior = num
    if menor is None or num < menor:
        menor = num

    # Perguntar se o usuário deseja continuar
    escolha = input('Deseja continuar? [S/N] ').strip().upper()
    while escolha not in ['S', 'N']:
        escolha = input('Resposta inválida! Digite S para continuar ou N para sair: ').strip().upper()

    # Se o usuário escolher 'N', encerrar o loop
    if escolha == 'N':
        break

# Calcular e mostrar a média
media = soma / cont
print(f'\nMédia entre todos os valores: {media}')
print(f'O maior número: {maior}')
print(f'O menor número: {menor}')
