import pygame

from settings import TILESIZE, WORLD_MAP

from tile import Tile
from player import Player

class Level:

    def __init__(self) -> None:

        # Get the display surface
        self.display_surface = pygame.display.get_surface()
        
        # Sprite group setup
        self.visible_sprites = pygame.sprite.Group()
        self.obstacles_sprites = pygame.sprite.Group()

        # Sprite setup
        self.create_map()

    def create_map(self) -> None:
        for row_index, row in enumerate(WORLD_MAP):
            for col_index, col in enumerate(row):
                x = col_index * TILESIZE
                y = row_index * TILESIZE

                if col == 'x':
                    Tile((x, y), [self.visible_sprites, self.obstacles_sprites])
                
                if col == 'p':
                    Player((x, y), [self.visible_sprites])

    def run(self):
        self.visible_sprites.draw(self.display_surface)