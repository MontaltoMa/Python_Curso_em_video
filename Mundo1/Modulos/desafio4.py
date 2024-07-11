# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome deles e escrevendo o do escolhido.

from random import choice

nomes = ["Black Panther", "Solid Snake", "Kendrick Lamar", "Shadow the Hedgehog"]

escolhido = choice(nomes)
print(f'O aluno escolhido e {escolhido}')

# Segunda opcao com o mesmo resultado usando o randint

from random import randint

nomes = ["Black Panther", "Solid Snake", "Kendrick Lamar", "Shadow the Hedgehog"]
escolha = randint(0, len(nomes) -1)

print(f'O aluno escolhido foi {nomes[escolha]}')