import pygame
from pygame.sprite import Sprite


class Cell(Sprite):
    def __init__(self, screen, xpos, ypos, cellSize, x_id, y_id):
        super().__init__() # Cell class inherits from Sprite

        self.screen = screen
        self.cellSize = cellSize
        self.x_id = x_id
        self.y_id = y_id

        self.color = (255, 255, 255) # Start out as white cell

        self.rect = pygame.Rect(xpos, ypos, self.cellSize,
                                self.cellSize)

    def draw_on_cell(self, game_state):
        self.color = game_state.draw_color

    def draw_cell(self):
        """Draw the bullet to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)