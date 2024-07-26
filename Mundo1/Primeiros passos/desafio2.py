# Faça um programa que leia algo pelo teclado 
# e mostre na tela o seu tipo primitivo 
# e todas as informações possíveis sobre ele

num = input("Digite algo: \n")

print("A entrada e um tipo: ", type(num))

print(f"E numerico? {num.isnumeric()}")
print(f'E alphanumerico? {num.isalpha()}')
print(f"É um decimal? {num.isdecimal()}")
print(f"Está em caixa baixa? {num.islower()}")
print(f"É apenas espaço em branco? {num.isspace()}")
print(f"Está em caixa alta? {num.isupper()}")