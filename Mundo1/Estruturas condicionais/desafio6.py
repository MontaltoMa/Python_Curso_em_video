'''
Faça um programa que leia três números e mostre qual é o maior e qual é o menor
'''

from random import randint

num1 = randint(0, 1000)
num2 = randint(0, 1000)
num3 = randint(0, 1000)

# verifica o maior numero entre os tres
if num1 > num2 and num1 > num3:
    maior = num1
elif num2 > num1 and num2 > num3:
    maior = num2
else:
    maior = num3

# verifica o menor numero entre os tres
if num1 < num2 and num1 < num3:
    menor = num1
elif num2 < num1 and num2 < num3:
    menor = num2
else:
    menor = num3

print(f'O maior numero dos tres e {maior}')
print(f'O menor numero dos tres e {menor}')