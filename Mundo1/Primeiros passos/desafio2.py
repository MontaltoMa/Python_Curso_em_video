# Faça um programa que leia algo pelo teclado 
# e mostre na tela o seu tipo primitivo 
# e todas as informações possíveis sobre ele

N = input("Digite algo: \n")

print("A entrada e um tipo: ", type(N))

print(f"E numerico? {N.isnumeric()}")
print(f'E alphanumerico? {N.isalpha()}')
print(f"É um decimal? {N.isdecimal()}")
print(f"Está em caixa baixa? {N.islower()}")
print(f"É apenas espaço em branco? {N.isspace()}")
print(f"Está em caixa alta? {N.isupper()}")