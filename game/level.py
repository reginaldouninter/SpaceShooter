import pygame
from config import LARGURA_TELA, ALTURA_TELA


class Level:
    def __init__(self, level_number):
        self.level_number = level_number
        self.background_image = None
        self.background_audio = None
        self.altura_tela = ALTURA_TELA  # Armazenar altura da tela
        self.load_level()

    def load_level(self):
        if self.level_number == 1:
            self.background_image = pygame.image.load("assets/BgLevel1.jpg")
            self.background_audio = "assets/level1.mp3"
        elif self.level_number == 2:
            self.background_image = pygame.image.load("assets/BgLevel2.jpg")
            self.background_audio = "assets/level2.wav"
        elif self.level_number == 3:
            self.background_image = pygame.image.load("assets/BgLevel3.jpg")
            self.background_audio = "assets/level3.wav"

    def start_level(self):
        pygame.mixer.music.load(self.background_audio)
        pygame.mixer.music.play(-1)  # Loop infinito

    def draw_background(self, tela, background_y):
        tela.blit(self.background_image, (0, background_y))
        tela.blit(self.background_image, (0, background_y - self.altura_tela))