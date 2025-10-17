import pygame
from pygame.font import Font
from pygame.rect import Rect
from pygame.surface import Surface

from code.Const import WIN_WIDTH, COLOR_RED, MENU_OPTIONS, COLOR_WHITE, COLOR_GRAY, COLOR_YELLOW


class Menu:

    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/MenuBg.png')
        self.rect = self.surf.get_rect()


    def run(self):
        menu_option = 0
        pygame.mixer_music.load('./asset/Menu.flac')
        pygame.mixer_music.play(-1)
        while True:
            self.window.blit(self.surf, self.rect)
            self.menu_text(60, "Aero Mission", COLOR_RED, ((WIN_WIDTH / 2), 90))

            for i in range(len(MENU_OPTIONS)):
                if i == menu_option:
                    self.menu_text(30, MENU_OPTIONS[i], COLOR_YELLOW, ((WIN_WIDTH / 2), 200 + 60 * i))
                else:
                    self.menu_text(30, MENU_OPTIONS[i], COLOR_GRAY, ((WIN_WIDTH / 2), 200 + 60 * i))

            pygame.display.flip()

        # Checar todos os eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit() #fechar janela
                    quit() # fim pygame
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        if menu_option < len(MENU_OPTIONS) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_UP:
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTIONS) - 1
                    if event.key == pygame.K_RETURN:
                        return MENU_OPTIONS[menu_option]



    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple, outline_color=(0, 0, 0), outline_thickness=2):
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