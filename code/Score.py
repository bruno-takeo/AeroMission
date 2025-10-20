from datetime import datetime
import sys

import pygame
from pygame.constants import KEYDOWN, K_RETURN, K_BACKSPACE, K_ESCAPE
from pygame.font import Font
from pygame.rect import Rect
from pygame.surface import Surface

from code.Const import WIN_WIDTH, WIN_HEIGHT, COLOR_YELLOW, SCORE_POS, MENU_OPTIONS, COLOR_WHITE
from code.DBProxy import DBProxy


class Score:

    def __init__(self, window: Surface):
        self.window = window
        self.surf = pygame.image.load('./asset/ScoreBg.png').convert_alpha()
        self.rect = self.surf.get_rect()
        # Redimensiona a imagem para ocupar toda a tela
        self.surf = pygame.transform.smoothscale(self.surf, (WIN_WIDTH, WIN_HEIGHT))
        # Centraliza na janela
        self.rect = self.surf.get_rect(center=(WIN_WIDTH // 2, WIN_HEIGHT // 2))

    def save(self, game_mode: str, player_score: list[int]):
        pygame.mixer_music.load('./asset/Score.wav')
        pygame.mixer_music.play(-1)
        db_proxy = DBProxy('DBScore')
        name = ''
        while True:
            self.window.blit(self.surf, self.rect)
            self.score_text(50, 'YOU WIN!', COLOR_YELLOW, SCORE_POS['Title'])
            if game_mode == MENU_OPTIONS[0]:
                score = player_score[0]
                text = 'Player 1 digite seu nome (4 caracteres): '
            if game_mode == MENU_OPTIONS[1]:
                score = (player_score[0] + player_score[1]) / 2
                text = 'Dupla Digite seu nome (4 caracteres): '
            if game_mode == MENU_OPTIONS[2]:
                if player_score[0] >= player_score[1]:
                    score = player_score[0]
                    text = 'Player 1 digite seu nome (4 caracteres): '
                else:
                    score = player_score[1]
                    text = 'Player 2 digite seu nome (4 caracteres): '
            self.score_text(22, text, COLOR_WHITE, SCORE_POS['EnterName'])

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_RETURN and len(name) == 4:
                        db_proxy.save({'name': name, 'score': score, 'date': get_formatted_date()})
                        self.show()
                        return
                    elif event.key == K_BACKSPACE:
                        name = name[:-1]
                    else:
                        if len(name) < 4:
                            name += event.unicode
            self.score_text(22, name, COLOR_WHITE, SCORE_POS['Name'])
            pygame.display.flip()
            pass

    def show(self):
        pygame.mixer_music.load('./asset/Score.wav')
        pygame.mixer_music.play(-1)
        self.window.blit(self.surf, self.rect)

        # Cabeçalhos
        self.score_text(50, 'TOP 10 SCORE', COLOR_YELLOW, SCORE_POS['Title'])
        self.score_text(22, 'NAME', COLOR_WHITE, (200, SCORE_POS['Label'][1]))
        self.score_text(22, 'SCORE', COLOR_WHITE, (400, SCORE_POS['Label'][1]))
        self.score_text(22, 'DATE', COLOR_WHITE, (650, SCORE_POS['Label'][1]))

        db_proxy = DBProxy('DBScore')
        list_score = db_proxy.retrieve_top10()
        db_proxy.close()

        # Coordenadas base
        start_y = SCORE_POS['Label'][1] + 40
        line_height = 35

        for i, player_score in enumerate(list_score):
            _, name, score, date = player_score
            y = start_y + i * line_height

            # Cada campo desenhado separadamente
            self.score_text(22, name, COLOR_WHITE, (200, y))
            self.score_text(22, f'{score:05d}', COLOR_WHITE, (400, y))
            self.score_text(22, date, COLOR_WHITE, (650, y))

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        return
            pygame.display.flip()


    def score_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple, outline_color=(0, 0, 0), outline_thickness=2):
        text_font: Font = pygame.font.SysFont('Trebuchet MS', text_size)
        text_surface: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surface.get_rect(center=text_center_pos)
        # Cria o contorno desenhando o texto várias vezes em torno da posição central
        for dx in range(-outline_thickness, outline_thickness + 1):
            for dy in range(-outline_thickness, outline_thickness + 1):
                if dx != 0 or dy != 0:
                    outline_surface: Surface = text_font.render(text, True, outline_color).convert_alpha()
                    outline_rect: Rect = outline_surface.get_rect(
                        center=(text_center_pos[0] + dx, text_center_pos[1] + dy))
                    self.window.blit(outline_surface, outline_rect)
        self.window.blit(text_surface, text_rect)

def get_formatted_date():
    current_datetime = datetime.now()
    current_time = current_datetime.strftime("%H:%M")
    current_date = current_datetime.strftime("%d/%m/%Y")
    return f'{current_time} - {current_date}'