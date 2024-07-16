''' Desenvolva um programa que leia nome, idade e sexo de 4 pessoas
No final do programa, mostre:
 - A média de idade do grupo
 - Qual é o nome do homem mais velho
 - Quantas mulheres têm menos de 20 anos
 '''

homem = ''
mulheres = 0
idades = []
soma_idades = 0
guardar_idade = 0

for i in range(4):
    nome = input('Digite seu primeiro nome: ').title()
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()

    if sexo != 'M' and sexo != 'F':
        print('O valor digitado para o campo Sexo é invalido!')
        break

    idades.append(idade)
    soma_idades += idade # Calcula todas as idades para devolver a média
    
    if sexo == 'M':
        if idade > idades[0]:
            homem = nome
            guardar_idade = idade
    elif sexo == 'F':
        if idade < 20:
            mulheres += 1
    elif sexo != 'M' or sexo != 'F':
        print('O valor digitado para o campo Sexo é invalido!')
else:
    print(f'A média das idades é {soma_idades / len(idades):.2f}')
    print(f'O nome do homem mais velho é {homem} com {guardar_idade}')

    if mulheres == 0:
        print('Nehuma das mulheres tem menos de 20 anos de idade.')
    else:
        print(f'{mulheres} tem menos de 20 anos de idade.')