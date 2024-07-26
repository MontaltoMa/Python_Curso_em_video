# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle

students = ["Black Panther", "Solid Snake", "Kendrick Lamar", "Shadow the Hedgehog"]
shuffle(students)
print(f'A ordem de apresentacao ficou: {students}')
