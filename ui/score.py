import pygame
from config import LARGURA_TELA, ALTURA_TELA, PRETO, BRANCO


class ScoreScreen:
    def __init__(self, tela, db_proxy):
        self.tela = tela
        self.db_proxy = db_proxy

    def show_scores(self):
        scores_ativos = True
        while scores_ativos:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if evento.type == pygame.KEYDOWN and evento.key == pygame.K_RETURN:
                    scores_ativos = False

            self.tela.fill(PRETO)
            fonte = pygame.font.Font(None, 74)
            texto_scores = fonte.render("Top Scores", True, BRANCO)
            self.tela.blit(texto_scores, (250, 50))

            top_scores = self.db_proxy.get_top_scores()
            fonte_pequena = pygame.font.Font(None, 36)

            for i, score in enumerate(top_scores):
                texto_score = fonte_pequena.render(f"{i + 1}. {score[0]} - {score[1]} - {score[2]} {score[3]}", True,
                                                   BRANCO)
                self.tela.blit(texto_score, (50, 150 + i * 40))

            texto_press_enter = fonte_pequena.render("Press Enter to return to menu", True, BRANCO)
            self.tela.blit(texto_press_enter, (200, ALTURA_TELA - 50))

            pygame.display.flip()