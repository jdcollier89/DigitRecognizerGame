import pygame
from pygame.sprite import Sprite


class Cell(Sprite):
    def __init__(self, screen, xpos, ypos, cellSize, x_id, y_id):
        super().__init__() # Cell class inherits from Sprite

        self.screen = screen
        self.cellSize = cellSize
        self.x_id = x_id
        self.y_id = y_id
        self.xpos = xpos
        self.ypos = ypos

        self.color = (255, 255, 255) # Start out as white cell
        self.fill_color = (0, 0, 0)

        self.draw_rect(self.cellSize)
        #self.rect = pygame.Rect(xpos, ypos, self.cellSize,
        #                        self.cellSize)

    def draw_on_cell(self, game_state):
        self.color = game_state.draw_color

    def draw_cell(self):
        """Draw the bullet to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)

    def return_drawn(self):
        if self.color == self.fill_color:
            output = 1
        else:
            output = 0
        return output

    def draw_rect(self, draw_size):
        self.rect = pygame.Rect(self.xpos, self.ypos, draw_size,
                                draw_size)
