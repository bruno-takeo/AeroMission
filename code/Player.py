import pygame
from code.Const import WIN_WIDTH, WIN_HEIGHT, ENTITY_SPEED, PLAYER_KEY_UP, PLAYER_KEY_DOWN, PLAYER_KEY_LEFT, \
    PLAYER_KEY_RIGHT, PLAYER_KEY_SHOOT, ENTITY_SHOT_DELAY
from code.Entity import Entity
from code.PlayerShot import PlayerShot


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        # não chama o super().__init__() ainda — para evitar carregar "Player1.png"
        self.name = name
        self.position = position
        self.speed = ENTITY_SPEED.get(self.name, 5)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]

        # --- Escala ---
        escala = 0.4

        # --- Animações ---
        self.animations = {
            "straight": [pygame.image.load(f"./asset/{self.name.lower()}_straight_{i}.png").convert_alpha() for i in range(4)],
            "up": [pygame.image.load(f"./asset/{self.name.lower()}_up_{i}.png").convert_alpha() for i in range(4)],
            "down": [pygame.image.load(f"./asset/{self.name.lower()}_down_{i}.png").convert_alpha() for i in range(4)]
        }

        # Redimensiona todas as imagens
        for key in self.animations:
            self.animations[key] = [
                pygame.transform.scale(img, (int(img.get_width() * escala), int(img.get_height() * escala)))
                for img in self.animations[key]
            ]

        # Começa reto
        self.current_state = "straight"
        self.frame_index = 0
        self.animation_timer = 0
        self.frame_delay = 100  # ms entre frames
        self.surf = self.animations[self.current_state][self.frame_index]
        self.rect = self.surf.get_rect(midleft=position)

    def move(self):
        pressed_key = pygame.key.get_pressed()

        if pressed_key[PLAYER_KEY_UP[self.name]] and self.rect.top > 0:
            self.rect.centery -= self.speed
            self.current_state = "up"
        elif pressed_key[PLAYER_KEY_DOWN[self.name]] and self.rect.bottom < WIN_HEIGHT:
            self.rect.centery += self.speed
            self.current_state = "down"
        else:
            self.current_state = "straight"

        if pressed_key[PLAYER_KEY_LEFT[self.name]] and self.rect.left > 0:
            self.rect.centerx -= self.speed
        if pressed_key[PLAYER_KEY_RIGHT[self.name]] and self.rect.right < WIN_WIDTH:
            self.rect.centerx += self.speed

        self.animate()

    def animate(self):
        now = pygame.time.get_ticks()
        if now - self.animation_timer > self.frame_delay:
            self.frame_index = (self.frame_index + 1) % len(self.animations[self.current_state])
            self.animation_timer = now

        self.surf = self.animations[self.current_state][self.frame_index]

    def get_shot_position(self):
        if self.name == 'Player1':
            return (self.rect.centerx + 85, self.rect.centery)  # offsets ajustados para Player1
        elif self.name == 'Player2':
            return (self.rect.centerx + 10, self.rect.centery - 125)  # offsets ajustados para Player2

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            pressed_key = pygame.key.get_pressed()
            if pressed_key[PLAYER_KEY_SHOOT[self.name]]:
                return PlayerShot(f'{self.name}Shot', self.get_shot_position())






