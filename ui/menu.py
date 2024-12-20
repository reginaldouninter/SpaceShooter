import pygame
from config import LARGURA_TELA, ALTURA_TELA, PRETO, BRANCO, AMARELO

class Menu:
    def __init__(self, tela):
        self.tela = tela
        self.menu_ativo = True
        self.opcoes_menu = ["Start Game", "Score", "Exit"]
        self.opcao_selecionada = 0
        self.background_menu = pygame.image.load("assets/BgMenu.jpg").convert()
        pygame.mixer.music.load("assets/menu.wav")
        pygame.mixer.music.play(-1)
        self.fonte_titulo = pygame.font.SysFont("Comic Sans MS", 72)
        self.fonte_opcoes = pygame.font.SysFont("Comic Sans MS", 48)


    def show_menu(self):
       self.menu_ativo = True
       while self.menu_ativo:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP:
                    self.opcao_selecionada -= 1
                    if self.opcao_selecionada < 0:
                        self.opcao_selecionada = len(self.opcoes_menu) - 1
                if evento.key == pygame.K_DOWN:
                    self.opcao_selecionada += 1
                    if self.opcao_selecionada >= len(self.opcoes_menu):
                        self.opcao_selecionada = 0
                if evento.key == pygame.K_RETURN:
                    pygame.mixer.music.stop()  # Para a música do menu
                    self.menu_ativo = False
                    if self.opcao_selecionada == 0:
                        return "start"
                    elif self.opcao_selecionada == 1:
                        return "score"
                    elif self.opcao_selecionada == 2:
                        return "exit"
        self.tela.blit(self.background_menu, (0, 0))
        texto_titulo = self.fonte_titulo.render("Space Shooter", True, BRANCO)
        titulo_pos = texto_titulo.get_rect(center=(LARGURA_TELA // 2, 100))
        self.tela.blit(texto_titulo, titulo_pos)
        for i, opcao in enumerate(self.opcoes_menu):
            if i == self.opcao_selecionada:
                texto = self.fonte_opcoes.render(opcao, True, AMARELO)
            else:
                texto = self.fonte_opcoes.render(opcao, True, BRANCO)
            opcao_pos = texto.get_rect(center=(LARGURA_TELA // 2, 250 + i * 70))
            self.tela.blit(texto, opcao_pos)

        pygame.display.update()