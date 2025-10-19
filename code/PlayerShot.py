import pygame

from code.Const import ENTITY_SPEED
from code.Entity import Entity


class PlayerShot(Entity):

    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

        # --- Redimensiona apenas o shot do Player1 ---
        if name == 'Player1Shot':
            escala = 0.6  # ajuste o valor para ficar menor
            width = int(self.surf.get_width() * escala)
            height = int(self.surf.get_height() * escala)
            self.surf = pygame.transform.scale(self.surf, (width, height))
            self.rect = self.surf.get_rect(center=position)  # redefine o rect após redimensionar

    def move(self):
        self.rect.centerx += ENTITY_SPEED[self.name]