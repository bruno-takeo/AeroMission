import pygame

from code.Const import WIN_WIDTH, WIN_HEIGHT, ENTITY_SPEED
from code.Entity import Entity


class Background(Entity):

    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

        # Redimensiona automaticamente para o tamanho da janela
        self.surf = pygame.transform.scale(self.surf, (WIN_WIDTH, WIN_HEIGHT))
        self.rect = self.surf.get_rect(topleft=position)

    def move(self, ):
        self.rect.centerx -= ENTITY_SPEED[self.name]
        if self.rect.right <= 0:
            self.rect.left = WIN_WIDTH