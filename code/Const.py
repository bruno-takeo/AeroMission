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
                'Player2': 3,
                'Enemy1': 2,
                'Enemy2': 4
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
PLAYER_SHOOT = {'Player1': pygame.K_RCTRL,
                 'Player2': pygame.K_LCTRL}

# S
SPAWN_TIME = 4000

# W
WIN_WIDTH = 930
WIN_HEIGHT = 523