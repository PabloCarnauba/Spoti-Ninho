import os
import pygame
import musica
import time

pygame.mixer.init()

class Player:

    def __init__(self, musica):

        self.musica = musica

    def start(self):

        pygame.mixer.music.load(self.musica.file)

        pygame.mixer.music.play()

    def pausar(self):

        pygame.mixer.music.pause()

    def despausar(self):

        pygame.mixer.music.unpause()

    def parar(self):

        pygame.mixer.music.stop()