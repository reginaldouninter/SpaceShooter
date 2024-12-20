import pygame

class Tiro:
    def __init__(self, x, y):
        self.image = pygame.image.load("assets/PlayerShot.png")
        self.x = x
        self.y = y
        self.y_mudanca = -5
        self.visivel = False

    def desenhar(self, tela):
        if self.visivel:
            tela.blit(self.image, (self.x, self.y))

    def mover(self):
        if self.visivel:
            self.y += self.y_mudanca
            if self.y < 0:
                self.visivel = False