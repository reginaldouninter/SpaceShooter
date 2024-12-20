import random

import pygame
from config import LARGURA_TELA, ALTURA_TELA, PRETO
from ui.menu import Menu
from ui.score import ScoreScreen
from ui.gameover import GameOverScreen, YouWinScreen
from game.level import Level
from game.player import Jogador
from game.enemy import Inimigo
from game.shot import Tiro
from database.db_proxy import DBProxy
from game.collision import colisao


class Game:
    def __init__(self):
        pygame.init()
        self.tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
        pygame.display.set_caption("Galaga Clone")
        self.db_proxy = DBProxy()
        self.menu = Menu(self.tela)
        self.score_screen = ScoreScreen(self.tela, self.db_proxy)
        self.game_over_screen = GameOverScreen(self.tela, self.db_proxy)
        self.you_win_screen = YouWinScreen(self.tela, self.db_proxy)
        self.jogador = None
        self.tiros_jogador = None
        self.inimigos = None
        self.level = None
        self.level_number = 1
        self.tempo_inicial = None
        self.tempo_de_level = 30
        self.background_y = 0
        self.executando = False

    def run(self):
        while True:
            escolha_menu = self.menu.show_menu()
            if escolha_menu == "start":
                self.start_game()
                self.game_loop()
            elif escolha_menu == "score":
                self.score_screen.show_scores()
            elif escolha_menu == "exit":
                pygame.quit()
                quit()

    def start_game(self):
        # Inicializar entidades
        self.jogador = Jogador(370, 480)
        self.tiros_jogador = []
        self.level_number = 1
        self.level = Level(self.level_number)
        self.level.start_level()
        self.tempo_inicial = pygame.time.get_ticks()
        self.background_y = 0  # Variável para controlar a posição da imagem de fundo
        self.inimigos = [Inimigo(self.level_number) for _ in range(6 + self.level_number)]
        self.executando = True

    def game_loop(self):
        while self.executando:
            tempo_atual = pygame.time.get_ticks()
            tempo_restante = self.tempo_de_level - ((tempo_atual - self.tempo_inicial) // 1000)
            tempo_fonte = pygame.font.Font(None, 36)
            if tempo_restante <= 0:
                if self.level_number < 3:
                    # Reinicia o nível e aumenta a dificuldade.
                    self.level_number += 1
                    self.level = Level(self.level_number)
                    self.level.start_level()
                    self.jogador.pontos += 1000
                    self.tempo_inicial = pygame.time.get_ticks()  # Reseta o tempo.
                    tempo_restante = 30
                    self.inimigos = [Inimigo(self.level_number) for _ in
                                     range(6 + self.level_number)]  # recria a lista ao passar de nível
                elif self.level_number == 3:
                    resultado = self.you_win_screen.you_win_screen(self.jogador.pontos)
                    if resultado == "menu":
                        self.executando = False

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    self.executando = False

                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_LEFT:
                        self.jogador.x_mudanca = -3  # Ajuste de velocidade do jogador
                    if evento.key == pygame.K_RIGHT:
                        self.jogador.x_mudanca = 3  # Ajuste de velocidade do jogador

                # Atirar ao pressionar a tecla Space
                keys_pressed = pygame.key.get_pressed()
                if keys_pressed[pygame.K_SPACE]:
                    novo_tiro_jogador = Tiro(self.jogador.x + 16, self.jogador.y)
                    novo_tiro_jogador.visivel = True
                    self.tiros_jogador.append(novo_tiro_jogador)

                if evento.type == pygame.KEYUP:
                    if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                        self.jogador.x_mudanca = 0

            self.jogador.mover()

            for tiro in self.tiros_jogador:
                tiro.mover()

            for inimigo in self.inimigos:
                inimigo.mover()
                inimigo.mover_tiro()
                inimigo.atirar()
                for tiro in self.tiros_jogador:
                    if tiro.visivel and colisao(tiro.x, tiro.y, inimigo.x, inimigo.y):
                        tiro.visivel = False
                        inimigo.x = random.randint(0, LARGURA_TELA - 64)
                        inimigo.y = random.randint(50, 150)
                        self.jogador.pontos += 100
                if colisao(inimigo.tiro_x, inimigo.tiro_y, self.jogador.x + 32, self.jogador.y + 32):
                    self.jogador.vidas -= 1
                    inimigo.tiro_visivel = False
                    if self.jogador.vidas <= 0:
                        resultado = self.game_over_screen.game_over_screen(self.jogador.pontos)
                        if resultado == "menu":
                            self.executando = False

            # Movimento do fundo
            self.background_y += 1  # Velocidade de rolagem, ajuste conforme necessário
            if self.background_y >= ALTURA_TELA:  # verifica se a imagem já saiu da tela
                self.background_y = 0  # reseta a imagem para o topo.

            self.level.draw_background(self.tela,
                                       self.background_y)  # passa o y de controle para a função draw_background
            self.jogador.desenhar(self.tela)
            self.jogador.desenhar_vidas(self.tela, pygame.font.Font(None, 36))
            self.jogador.desenhar_pontos(self.tela, pygame.font.Font(None, 36))
            self.exibir_tempo_restante(tempo_fonte, tempo_restante)

            for tiro in self.tiros_jogador:
                tiro.desenhar(self.tela)

            for inimigo in self.inimigos:
                inimigo.desenhar(self.tela)

            pygame.display.update()

    def exibir_tempo_restante(self, font, tempo):
        texto_tempo = font.render(f"Tempo: {tempo}", True, (255, 255, 255))
        self.tela.blit(texto_tempo, (LARGURA_TELA - texto_tempo.get_width() - 10, 10))