'''
Escreva um programa para aprovar o empréstimo bancário
para a compra de uma casa
O programa vai perguntar o valor da casa, o salário do comprador e em quantos
anos ele vai pagar

Calcule o valor da prestação mensal,
sabendo que ela não pode exceder 30% do salário
ou então o empréstimo será negado
'''
def calc_portion(valor_casa, anos):
    return valor_casa / (anos * 12)

def min_percentage(salario):
    return salario * 0.30

home_value = float(input('Digite o valor da casa que vai comprar: \nR$'))
salari = float(input(('Digite seu salario atual \nR$')))
year = int(input(('Digite em quantos anos gostaria de financiar: \n')))

portion = calc_portion(home_value, year)
percentage = min_percentage(salari)

if salari == 0 or home_value == 0:
    print(f'Algo deu errado confirme se o valor da casa R${home_value:.2f} e o salario R${salari:.2f} estao corretos, lembrando que nao podem ser Zero ou Negativos')
elif portion <= percentage:
    print(f'O valor da casa é de R${home_value:.2f} e seu salário é R${salari:.2f}. Sendo assim, é possível parcelar a casa.')
else:
    print(f'Infelizmente seu salário de R${salari:.2f} é muito baixo para financiar esta casa de R${home_value:.2f}.')