# C
import pygame

COLOR_RED = (220, 20, 60)
COLOR_WHITE = (245, 245, 245)
COLOR_GRAY = (224, 224, 224)
COLOR_YELLOW = (255, 215, 0)
COLOR_GREEN = (0, 128, 0)
COLOR_CYAN = (0, 128, 128)

# E
EVENT_ENEMY = pygame.USEREVENT + 1
EVENT_TIMEOUT = pygame.USEREVENT + 2
ENTITY_SPEED = {
                'Level1Bg4': 0,
                'Level1Bg3': 1,
                'Level1Bg2': 3,
                'Level1Bg1': 3,
                'Level1Bg0': 5,
                'Level2Bg8': 0,
                'Level2Bg7': 1,
                'Level2Bg6': 2,
                'Level2Bg5': 3,
                'Level2Bg4': 4,
                'Level2Bg3': 5,
                'Level2Bg2': 6,
                'Level2Bg1': 7,
                'Level2Bg0': 8,
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
                 'Level2Bg8': 999,
                 'Level2Bg7': 999,
                 'Level2Bg6': 999,
                 'Level2Bg5': 999,
                 'Level2Bg4': 999,
                 'Level2Bg3': 999,
                 'Level2Bg2': 999,
                 'Level2Bg1': 999,
                 'Level2Bg0': 999,
                 'Player1': 300,
                 'Player1Shot': 1,
                 'Player2': 300,
                 'Player2Shot': 1,
                 'Enemy1': 80,
                 'Enemy1Shot': 1,
                 'Enemy2': 60,
                 'Enemy2Shot': 1
}

ENTITY_SCORE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level1Bg4': 0,
    'Level2Bg8': 0,
    'Level2Bg7': 0,
    'Level2Bg6': 0,
    'Level2Bg5': 0,
    'Level2Bg4': 0,
    'Level2Bg3': 0,
    'Level2Bg2': 0,
    'Level2Bg1': 0,
    'Level2Bg0': 0,
    'Player1': 0,
    'Player1Shot': 0,
    'Player2': 0,
    'Player2Shot': 0,
    'Enemy1': 100,
    'Enemy1Shot': 0,
    'Enemy2': 125,
    'Enemy2Shot': 0
}

ENTITY_SHOT_DELAY = {
                    'Player1': 30,
                    'Player2': 50,
                    'Enemy1': 140,
                    'Enemy2': 80,
}

ENEMY_SHOT_OFFSET = {
    'Enemy1': -30,  # ajuste pixels para centralizar visualmente
    'Enemy2': -10
}

ENTITY_DAMAGE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level1Bg4': 0,
    'Level2Bg8': 0,
    'Level2Bg7': 0,
    'Level2Bg6': 0,
    'Level2Bg5': 0,
    'Level2Bg4': 0,
    'Level2Bg3': 0,
    'Level2Bg2': 0,
    'Level2Bg1': 0,
    'Level2Bg0': 0,
    'Player1': 1,
    'Player1Shot': 30,
    'Player2': 1,
    'Player2Shot': 45,
    'Enemy1': 1,
    'Enemy1Shot': 63,
    'Enemy2': 1,
    'Enemy2Shot': 63
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


SPAWN_TIME = 1500

# T
TIMEOUT_STEP = 100
TIMEOUT_LEVEL = 40000

# W
WIN_WIDTH = 930
WIN_HEIGHT = 523

# S
SCORE_POS = {
    'Title': (WIN_WIDTH / 2, 50),
    'EnterName': (WIN_WIDTH / 2, 110),
    'Label': (WIN_WIDTH / 2, 110),
    'Name': (WIN_WIDTH / 2, 150),
    0: (WIN_WIDTH / 2, 150),
    1: (WIN_WIDTH / 2, 180),
    2: (WIN_WIDTH / 2, 210),
    3: (WIN_WIDTH / 2, 240),
    4: (WIN_WIDTH / 2, 270),
    5: (WIN_WIDTH / 2, 300),
    6: (WIN_WIDTH / 2, 330),
    7: (WIN_WIDTH / 2, 360),
    8: (WIN_WIDTH / 2, 390),
    9: (WIN_WIDTH / 2, 420),
}