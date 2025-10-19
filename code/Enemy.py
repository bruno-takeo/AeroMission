import pygame
from code.Const import ENTITY_SPEED, WIN_WIDTH, ENTITY_HEALTH, ENTITY_SHOT_DELAY, ENEMY_SHOT_OFFSET
from code.EnemyShot import EnemyShot
from code.Entity import Entity

class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        # não chama o super().__init__() ainda
        self.name = name
        self.position = position
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]

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

        # --- Velocidade e vida ---
        self.speed = ENTITY_SPEED.get(self.name, 3)
        self.health = ENTITY_HEALTH.get(self.name, 1)

    def move(self):
        # Movimento simples da direita para a esquerda
        self.rect.centerx -= ENTITY_SPEED[self.name]

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            offset_y = ENEMY_SHOT_OFFSET.get(self.name, 0)
            return EnemyShot(f'{self.name}Shot', (self.rect.centerx - 150, self.rect.centery + offset_y))