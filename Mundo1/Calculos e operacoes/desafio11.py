# Conversor de temperaturas: escreva um programa que converta uma temperatura digitada em ºC para ºF

n = float(input('Digite a temperatura atual: \n'))

conversao = (n * 1.8 ) + 32

print(f'A temperatura de graus {n}°C em Fahrenheit e = {conversao}°F')