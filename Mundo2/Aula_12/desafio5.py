'''
Crie um programa que leia duas notas de um aluno e calcule sua média,
mostrando uma mensagem no final, de acordo com a média atingida:

- média abaixo de 5.0: reprovado
- média entre 5.0 e 6,9: recuperação
- média 7.0 ou superior: aprovado
'''
print('Vamos calucular sua media!')
nota1 = float(input(('Digite sua primeira nota:\n')))
nota2 = float(input(('Digite sua segunda nota:\n')))


def calcular_media(nota1, nota2):
    return (nota1 + nota2) / 2

avg = calcular_media(nota1, nota2)

if avg < 5:
    print(f'Sua média foi {avg:.1f} sendo {avg - 5} pontos abaixo de 5.0: reprovado')
elif 5 <= avg < 7:
    print(f'Su média foi {avg:.1f}: recuperação')
else:
    print(f'Sua média foi {avg:.1f}: aprovado')