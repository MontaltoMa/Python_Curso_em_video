# Conversor de temperaturas: escreva um programa que converta uma temperatura digitada em ºC para ºF

num = float(input('Digite a temperatura atual: \n'))

conversion = (num * 1.8 ) + 32

print(f'A temperatura de graus {num}°C em Fahrenheit e = {conversion}°F')