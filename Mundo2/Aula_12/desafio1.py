'''
Escreva um programa para aprovar o empréstimo bancário
para a compra de uma casa
O programa vai perguntar o valor da casa, o salário do comprador e em quantos
anos ele vai pagar

Calcule o valor da prestação mensal,
sabendo que ela não pode exceder 30% do salário
ou então o empréstimo será negado
'''
def calcular_parcela(valor_casa, anos):
    return valor_casa / (anos * 12)

def porcentagem_minima(salario):
    return salario * 0.30

valor_casa = float(input('Digite o valor da casa que vai comprar: \nR$'))
salario = float(input(('Digite seu salario atual \nR$')))
anos = int(input(('Digite em quantos anos gostaria de financiar: \n')))

parcela = calcular_parcela(valor_casa, anos)
porcentagem = porcentagem_minima(salario)

if salario == 0 or valor_casa == 0:
    print(f'Algo deu errado confirme se o valor da casa R${valor_casa:.2f} e o salario R${salario:.2f} estao corretos, lembrando que nao podem ser Zero ou Negativos')
elif parcela <= porcentagem:
    print(f'O valor da casa é de R${valor_casa:.2f} e seu salário é R${salario:.2f}. Sendo assim, é possível parcelar a casa.')
else:
    print(f'Infelizmente seu salário de R${salario:.2f} é muito baixo para financiar esta casa de R${valor_casa:.2f}.')