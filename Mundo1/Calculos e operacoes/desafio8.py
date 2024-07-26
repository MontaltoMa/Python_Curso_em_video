# Faça um programa que leia a largura e a algura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m²

height = float(input('Digite a altura da parde: \n'))
width = float(input('Digite a largura da parede: \n'))

avg = height * width

print(f'Sua parede tem uma dimensao de {height}M X {width}M, tendo uma area total de {avg}\n')

amount = avg / 2
print(f'Voce ira precisar de mais ou menos {amount:.2f} litros de tinta para pintar sua parede')