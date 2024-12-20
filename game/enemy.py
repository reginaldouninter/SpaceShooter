import pygame
import random

class Inimigo:
    def __init__(self, level=1):
        self.images = [
            pygame.image.load("assets/enemy1.png"),
            pygame.image.load("assets/enemy2.png"),
            pygame.image.load("assets/enemy3.png")
        ]
        self.image = random.choice(self.images)
        self.x = random.randint(0, 800 - 64)
        self.y = random.randint(50, 150)
        self.x_mudanca = 1 + (level - 1) * 0.2  # Ajustando o aumento de velocidade
        self.y_mudanca = 10 + (level - 1) * 1  # Ajustando o aumento de velocidade
        self.tiro_img = pygame.image.load(f"assets/EnemyShot{random.randint(1,3)}.png")
        self.tiro_x = 0
        self.tiro_y = self.y
        self.tiro_y_mudanca = 2 + (level - 1) * 0.2  # Ajustando o aumento de velocidade
        self.tiro_visivel = False
        self.tempo_ultimo_tiro = pygame.time.get_ticks()
        self.tempo_entre_tiros = 1000
        self.direction_change_interval = 2000
        self.last_direction_change = pygame.time.get_ticks()

    def desenhar(self, tela):
        tela.blit(self.image, (self.x, self.y))
        if self.tiro_visivel:
            tela.blit(self.tiro_img, (self.tiro_x, self.tiro_y))

    def mover(self):
        tempo_atual = pygame.time.get_ticks()
        if tempo_atual - self.last_direction_change >= self.direction_change_interval:
            self.x_mudanca *= -1
            self.last_direction_change = tempo_atual
        self.x += self.x_mudanca
        if self.x <= 0 or self.x >= 800 - 64:
            self.x_mudanca *= -1
            self.y += self.y_mudanca

    def atirar(self):
        tempo_atual = pygame.time.get_ticks()
        if not self.tiro_visivel and tempo_atual - self.tempo_ultimo_tiro >= self.tempo_entre_tiros:
            self.tiro_x = self.x + 16
            self.tiro_y = self.y
            self.tiro_visivel = True
            self.tempo_ultimo_tiro = tempo_atual

    def mover_tiro(self):
        if self.tiro_visivel:
            self.tiro_y += self.tiro_y_mudanca
            if self.tiro_y > 600:
                self.tiro_visivel = False