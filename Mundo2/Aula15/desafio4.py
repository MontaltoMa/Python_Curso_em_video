''' Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar
se o usuário quer ou não continuar.
No final, mostra:
a) quantas pessoas têm mais de 18 anos
b) quantos homens foram cadastrados
c) quantas mulheres têm menos de 20 anos'''

maior_idade = 0

homens = 0

mulheres = 0

while True:
    nome = str(input('Digite seu primeiro nome:\n')).strip().title()
    idade = int(input('Digite sua idade:\n'))
    sexo = str(input('Digite seu sexo [M/F]:\n')).strip().upper()

    if idade > 18:
        maior_idade +=1
    
    if sexo == 'M':
        homens += 1

    if sexo == 'F' and idade < 20:
            mulheres +=1

    continuar = str(input('Deseja cadastrar mais uma pessoa? [S/N]\n')).strip().upper()

    while continuar not in ['S', 'N']:
        continuar = str(input('Digite uma entrada valida [S/N]:\n')).strip().upper()

    if continuar == 'N':
        break

print(f'Foram cadastrados {maior_idade} pessoas maiores de 18 anos!')
print(f'Foram cadastrados {homens} homens!')
print(f'Foram cadastrados {mulheres} mulheres menores de 20 anos!')