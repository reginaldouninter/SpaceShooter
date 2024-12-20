import pygame
class Jogador:
    def __init__(self, x, y):
        self.image = pygame.image.load("assets/player.png")
        self.x = x
        self.y = y
        self.x_mudanca = 0
        self.vidas = 10
        self.pontos = 0

    def desenhar(self, tela):
        tela.blit(self.image, (self.x, self.y))

    def mover(self):
        self.x += self.x_mudanca
        if self.x <= 0:
            self.x = 0
        elif self.x >= 800 - 64:
            self.x = 800 - 64

    def desenhar_vidas(self, tela, fonte):
        texto_vidas = fonte.render(f"Vidas: {self.vidas}", True, (255, 255, 255))
        tela.blit(texto_vidas, (10, 10))

    def desenhar_pontos(self, tela, fonte):
        texto_pontos = fonte.render(f"Pontos: {self.pontos}", True, (255, 255, 255))
        tela.blit(texto_pontos, (10, 50))