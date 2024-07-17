'''
r = "S"
n = 1
while r == "S":
    n = int(input("Digite um valor: \n"))
    r = str(input("Quer continuar? [S/N] \n")).upper()
print("Você digitou {}, que é a condição de parada.".format(r))
'''

resp = 'S'
num = 1

while resp == "S":
    num = int(input("Digite um valor: \n"))
    resp = str(input("Quer continuar? [S/N]")).upper()
print(f"Você digitou {resp}, que é a condição")
print(f'O ultimo numero digitado foi {num}')