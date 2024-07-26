name = "Mitsurugi"

print(f"Prazer em te conhecer, {name:20}!")
print(f"Prazer em te conhecer, {name:>20}!")
print(f"Prazer em te conhecer, {name:<20}!")
print(f"Prazer em te conhecer, {name:^20}!")
print(f"Prazer em te conhecer, {name:=^20}!")

num1 = int(input("Um valor: \n"))
num2 = int(input("Outro valor: \n"))
s = num1 + num2
m = num1 * num2
d = num1 / num2
di = num1 // num2
e = num1 ** num2

print(f"A soma é {s}, \no produto é {m} \ne a divisão é {d:.3f}")
print(f"\nDivisão inteira: {di} \ne potência: {e}.")