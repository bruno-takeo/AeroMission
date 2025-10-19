import pygame
from code.Const import ENTITY_SPEED, WIN_WIDTH
from code.Entity import Entity

class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        # não chama o super().__init__() ainda
        self.name = name
        self.position = position

        # --- Escala ---
        escala = 0.35  # ajuste conforme necessário

        # --- Carrega a imagem ---
        self.surf = pygame.image.load(f"./asset/{self.name.lower()}.png").convert_alpha()

        # --- Redimensiona ---
        width = int(self.surf.get_width() * escala)
        height = int(self.surf.get_height() * escala)
        self.surf = pygame.transform.scale(self.surf, (width, height))

        # --- Define o rect ---
        self.rect = self.surf.get_rect(midleft=position)

        # --- Velocidade ---
        self.speed = ENTITY_SPEED.get(self.name, 3)

    def move(self):
        # Movimento simples da direita para a esquerda
        self.rect.centerx -= self.speed
        if self.rect.right <= 0:
            self.rect.left = WIN_WIDTH
