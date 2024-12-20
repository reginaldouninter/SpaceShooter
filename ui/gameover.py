import pygame
from config import LARGURA_TELA, ALTURA_TELA, PRETO, BRANCO, VERDE

class GameOverScreen:
    def __init__(self, tela, db_proxy):
        self.tela = tela
        self.db_proxy = db_proxy
        self.input_box = pygame.Rect(250, 400, 300, 50)
        self.cor_ativa = pygame.Color('lightskyblue3')
        self.cor_inativa = pygame.Color('dodgerblue2')
        self.cor = self.cor_inativa
        self.ativo = False
        self.nome = ''
        self.fonte = pygame.font.Font(None, 74)

    def game_over_screen(self, pontos):
      self.ativo = False
      self.nome = ''
      game_over = True
      while game_over:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    if self.input_box.collidepoint(evento.pos):
                        self.ativo = not self.ativo
                    else:
                        self.ativo = False
                    self.cor = self.cor_ativa if self.ativo else self.cor_inativa
                if evento.type == pygame.KEYDOWN:
                    if self.ativo:
                        if evento.key == pygame.K_RETURN:
                            self.db_proxy.add_score(self.nome, pontos)
                            return "menu"
                        elif evento.key == pygame.K_BACKSPACE:
                           self.nome = self.nome[:-1]
                        else:
                           self.nome += evento.unicode

            self.tela.fill(PRETO)
            texto_game_over = self.fonte.render("Game Over!", True, BRANCO)
            self.tela.blit(texto_game_over, (250, 200))
            texto_nome = self.fonte.render("Enter your name: ", True, BRANCO)
            self.tela.blit(texto_nome, (250, 300))
            txt_surface = self.fonte.render(self.nome, True, self.cor)
            largura_max_input_box = max(300, txt_surface.get_width() + 10)
            self.input_box.w = largura_max_input_box
            self.tela.blit(txt_surface, (self.input_box.x + 5, self.input_box.y + 5))
            pygame.draw.rect(self.tela, self.cor, self.input_box, 2)

            pygame.display.flip()

class YouWinScreen:
    def __init__(self, tela, db_proxy):
       self.tela = tela
       self.db_proxy = db_proxy
       self.input_box = pygame.Rect(250, 400, 300, 50)
       self.cor_ativa = pygame.Color('lightskyblue3')
       self.cor_inativa = pygame.Color('dodgerblue2')
       self.cor = self.cor_inativa
       self.ativo = False
       self.nome = ''
       self.fonte = pygame.font.Font(None, 74)

    def you_win_screen(self, pontos):
       self.ativo = False
       self.nome = ''
       you_win = True

       while you_win:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                   pygame.quit()
                   quit()
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    if self.input_box.collidepoint(evento.pos):
                        self.ativo = not self.ativo
                    else:
                        self.ativo = False
                    self.cor = self.cor_ativa if self.ativo else self.cor_inativa
                if evento.type == pygame.KEYDOWN:
                    if self.ativo:
                        if evento.key == pygame.K_RETURN:
                            self.db_proxy.add_score(self.nome, pontos)
                            return "menu"
                        elif evento.key == pygame.K_BACKSPACE:
                             self.nome = self.nome[:-1]
                        else:
                             self.nome += evento.unicode

            self.tela.fill(PRETO)
            texto_game_over = self.fonte.render("You Win!!!", True, VERDE)
            self.tela.blit(texto_game_over, (250, 200))
            texto_nome = self.fonte.render("Enter your name: ", True, BRANCO)
            self.tela.blit(texto_nome, (250, 300))
            txt_surface = self.fonte.render(self.nome, True, self.cor)
            largura_max_input_box = max(300, txt_surface.get_width() + 10)
            self.input_box.w = largura_max_input_box
            self.tela.blit(txt_surface, (self.input_box.x + 5, self.input_box.y + 5))
            pygame.draw.rect(self.tela, self.cor, self.input_box, 2)
            pygame.display.flip()