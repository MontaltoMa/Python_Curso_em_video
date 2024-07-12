'''
Escreva um programa que leia dois números inteiros e compare-os,
mostrando na tela uma mensagem:
- o primeiro valor é maior
- o segundo valor é maior
- não existe valor maior; os dois são iguais
'''
def comparando_valores(num1, num2):
    if num1 > num2:
        return 'Primeiro valor é maior'
    elif num1 < num2:
        return 'Segundo valor é maior'
    else:
        return 'Não existe valor maior, ambos sao iguais'
    
print('Vamos comparar dois numeros inteiros para ver qual e maior')
num1 = int(input('Digite o primeiro valor: \n'))
num2 = int(input('Digite o segundo valor: \n'))

resultado = comparando_valores(num1, num2)

print(resultado)