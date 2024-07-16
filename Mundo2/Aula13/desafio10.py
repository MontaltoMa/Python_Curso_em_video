''' Faça um programa que leia o peso de cinco pessoas
No final, mostre qual foi o maior e o menor peso lidos'''

maior = 0
menor = float('inf')

for i in range(5):
    peso = float(input('Digite seu peso: \nKG'))
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso

print(f'O maior peso digitado e {maior:.2f}')
print(f'O menor peso digitado e {menor:.2f}')