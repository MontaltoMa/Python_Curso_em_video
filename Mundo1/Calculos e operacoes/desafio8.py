# Faça um programa que leia a largura e a algura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m²

altura = float(input('Digite a altura da parde: \n'))
largura = float(input('Digite a largura da parede: \n'))

area = altura * largura

print(f'Sua parede tem uma dimensao de {altura}M X {largura}M, tendo uma area total de {area}\n')

quantidade_tinta = area / 2
print(f'Voce ira precisar de mais ou menos {quantidade_tinta:.2f} litros de tinta para pintar sua parede')