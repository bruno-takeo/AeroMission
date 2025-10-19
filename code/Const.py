# C
import pygame

COLOR_RED = (220, 20, 60)
COLOR_WHITE = (245, 245, 245)
COLOR_GRAY = (224, 224, 224)
COLOR_YELLOW = (255, 215, 0)

# E
EVENT_ENEMY = pygame.USEREVENT + 1
ENTITY_SPEED = {
                'Level1Bg4': 0,
                'Level1Bg3': 1,
                'Level1Bg2': 3,
                'Level1Bg1': 3,
                'Level1Bg0': 5,
                'Player1': 3,
                'Player1Shot': 2,
                'Player2': 3,
                'Player2Shot': 2,
                'Enemy1': 2,
                'Enemy1Shot': 5,
                'Enemy2': 4,
                'Enemy2Shot': 7,
                }

ENTITY_HEALTH = {
                 'Level1Bg0': 999,
                 'Level1Bg1': 999,
                 'Level1Bg2': 999,
                 'Level1Bg3': 999,
                 'Level1Bg4': 999,
                 'Player1': 300,
                 'Player1Shot': 1,
                 'Player2': 300,
                 'Player2Shot': 1,
                 'Enemy1': 60,
                 'Enemy1Shot': 90,
                 'Enemy2': 50,
                 'Enemy2Shot': 80
}

ENTITY_SHOT_DELAY = {
                    'Player1': 30,
                    'Player2': 50,
                    'Enemy1': 130,
                    'Enemy2': 70,
}

# Constantes
ENEMY_SHOT_OFFSET = {
    'Enemy1': -130,  # ajuste pixels para centralizar visualmente
    'Enemy2': -65
}


# M
MENU_OPTIONS = ('NEW GAME 1P',
                'NEW GAME 2P - COOPERATIVE',
                'NEW GAME 2P - COMPETITIVE',
                'SCORE',
                'EXIT')

# P
PLAYER_KEY_UP = {'Player1': pygame.K_UP,
                 'Player2': pygame.K_w}
PLAYER_KEY_DOWN = {'Player1': pygame.K_DOWN,
                 'Player2': pygame.K_s}
PLAYER_KEY_LEFT = {'Player1': pygame.K_LEFT,
                 'Player2': pygame.K_a}
PLAYER_KEY_RIGHT = {'Player1': pygame.K_RIGHT,
                 'Player2': pygame.K_d}
PLAYER_KEY_SHOOT = {'Player1': pygame.K_SPACE,
                 'Player2': pygame.K_LCTRL}

# S
SPAWN_TIME = 4000

# W
WIN_WIDTH = 930
WIN_HEIGHT = 523