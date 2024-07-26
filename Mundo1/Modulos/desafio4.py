# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome deles e escrevendo o do escolhido.

from random import choice

names = ["Black Panther", "Solid Snake", "Kendrick Lamar", "Shadow the Hedgehog"]

chosen = choice(names)
print(f'O aluno escolhido e {chosen}')

# Segunda opcao com o mesmo resultado usando o randint

from random import randint

names = ["Black Panther", "Solid Snake", "Kendrick Lamar", "Shadow the Hedgehog"]
chosen = randint(0, len(names) -1)

print(f'O aluno escolhido foi {names[chosen]}')