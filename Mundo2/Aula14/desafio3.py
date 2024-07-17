''' Crie um programa que leia dois valores e mostre um menu
na tela:

1: somar
2: multiplicar
3: maior
4: novos números
5: sair do programa

Seu programa deverá realizar a operação solicitada em cada caso '''

def soma (num1, num2):
    return num1 + num2

def multiplicar (num1, num2):
    return num1 * num2

def maior_numero(num1, num2):
    return max(num1, num2)

num1 = float(input('Digite o primeiro numero:\n'))
num2 = float(input('Digite o segundo numero:\n'))

while True:

    escolha = int(input('''Escolha uma funcao no nosso painel:
1: somar
2: multiplicar
3: maior
4: novos números
5: sair do programa\n'''))
    
    if escolha == 1:
        print(f'A soma entre {num1} + {num2} = {soma(num1, num2):.2f}\n')
    elif escolha == 2:
        print(f'A multiplicacao entre {num1} * {num2} = {multiplicar(num1, num2):.2f}\n')
    elif escolha == 3:
        if num1 == num2:
            print('Ambos tem o mesmo valor')
        else:
            print(f'O maior numero entre {num1} e {num2} e {maior_numero(num1, num2):.2f}')
    elif escolha == 4:
        print('Digite novos numeros!')
        num1 = float(input('Digite o primeiro numero:\n'))
        num2 = float(input('Digite o segundo numero:\n'))
        
    else:
        print('Escolha entre uma das opcoes do nosso menu! ')