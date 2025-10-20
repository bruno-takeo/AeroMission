import os
import random
import sys
import pygame
from pygame.font import Font
from pygame.rect import Rect
from pygame.surface import Surface

from code.Const import (
    COLOR_WHITE, WIN_HEIGHT, MENU_OPTIONS, EVENT_ENEMY, SPAWN_TIME,
    COLOR_GREEN, COLOR_CYAN, EVENT_TIMEOUT, TIMEOUT_STEP, TIMEOUT_LEVEL
)
from code.Enemy import Enemy
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator
from code.Player import Player


class Level:

    def __init__(self, window: Surface, name: str, game_mode: str, player_score: list[int]):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []

        # Cria jogadores
        player = EntityFactory.get_entity('Player1')
        player.score = player_score[0]
        self.entity_list.append(player)

        if game_mode in [MENU_OPTIONS[1], MENU_OPTIONS[2]]:
            player = EntityFactory.get_entity('Player2')
            player.score = player_score[1]
            self.entity_list.append(player)

        # Eventos e timeout
        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)
        pygame.time.set_timer(EVENT_TIMEOUT, TIMEOUT_STEP)

        # Adiciona o background por último (fica por baixo no reversed)
        self.entity_list.extend(EntityFactory.get_entity(self.name + 'Bg'))

        self.timeout = TIMEOUT_LEVEL

    def run(self, player_score: list[int]):
        # Música do nível
        music_path_mp3 = f'./asset/{self.name}.mp3'
        music_path_wav = f'./asset/{self.name}.wav'

        if os.path.exists(music_path_mp3):
            pygame.mixer_music.load(music_path_mp3)
        elif os.path.exists(music_path_wav):
            pygame.mixer_music.load(music_path_wav)
        else:
            print(f"Aviso: nenhuma música encontrada para {self.name}.")
            pygame.mixer_music.stop()
        pygame.mixer_music.play(-1)

        clock = pygame.time.Clock()

        # Loop principal
        while True:
            clock.tick(60)

            # --- Render e movimentação ---
            for ent in reversed(self.entity_list):
                self.window.blit(ent.surf, ent.rect)
                ent.move()

                # Disparo de inimigos e jogadores
                if isinstance(ent, (Player, Enemy)):
                    shoot = ent.shoot()
                    if shoot is not None:
                        # 🔹 Localiza o primeiro background na lista
                        first_bg_index = next(
                            (i for i, e in enumerate(self.entity_list) if 'Bg' in e.name),
                            len(self.entity_list)
                        )
                        # 🔹 Insere o tiro antes das camadas de background
                        self.entity_list.insert(first_bg_index, shoot)

                # HUD dos jogadores
                if ent.name == 'Player1':
                    self.level_text(14, f'Player1 - Health: {ent.health} | Score: {ent.score}', COLOR_GREEN, (10, 25))
                if ent.name == 'Player2':
                    self.level_text(14, f'Player2 - Health: {ent.health} | Score: {ent.score}', COLOR_CYAN, (10, 45))

            # --- Eventos do jogo ---
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == EVENT_ENEMY:
                    choice = random.choice(('Enemy1', 'Enemy2'))
                    self.entity_list.insert(1, EntityFactory.get_entity(choice))

                if event.type == EVENT_TIMEOUT:
                    self.timeout -= TIMEOUT_STEP
                    if self.timeout == 0:
                        for ent in self.entity_list:
                            if isinstance(ent, Player) and ent.name == 'Player1':
                                player_score[0] = ent.score
                            if isinstance(ent, Player) and ent.name == 'Player2':
                                player_score[1] = ent.score
                        return True

                # Verifica se o jogador morreu
                found_player = any(isinstance(ent, Player) for ent in self.entity_list)
                if not found_player:
                    return False

            # --- HUD e informações de debug ---
            self.level_text(14, f'{self.name} - Timeout: {self.timeout / 1000 :.1f}s', COLOR_WHITE, (10, 5))
            self.level_text(14, f'fps: {clock.get_fps():.0f}', COLOR_WHITE, (10, WIN_HEIGHT - 35))
            self.level_text(14, f'entidades: {len(self.entity_list)}', COLOR_WHITE, (10, WIN_HEIGHT - 20))

            pygame.display.flip()

            # --- Colisões e atualizações ---
            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont('Trebuchet MS', text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(text_surf, text_rect)
