# Faça um programa em Python que abra e reproduza um arquivo mp3

# importar a biblioteca pygame
from pygame import mixer

# uma forma de implementar o código
mixer.init()
# substitua o nome do arquivo "musica.mp3" pelo seu arquivo mp3
mixer.music.load('musica.mp3')
mixer.music.play()

x = input('Esta escutanndo?')

