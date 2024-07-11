""" Desenvolva um programa que leia o comprimento de três retas
 e diga ao usuário se elas podem ou não formar um triângulo

 Inclusive posso dizer qual tipo de triângulo pode ser formado.
 Não deve ser difícil isso em Python."""

reta1 = float(input('Digite o comprimento da primeira reta: '))
reta2 = float(input('Digite o comprimento da segunda reta: '))
reta3 = float(input('Digite o comprimento da terceira reta: '))

if reta1 + reta2 > reta3 and reta1 + reta3 > reta2 and reta2 + reta3 > reta1:
    print('O triangulo existe!')
else:
    print('O triangulo nao pode existe')