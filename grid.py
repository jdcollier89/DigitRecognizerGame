import numpy as np
import pygame
from pygame.sprite import Sprite, Group
from cell import Cell


class Grid:

    def __init__(self, boxSize, xPos, yPos, screen):
        self.pos = (xPos, yPos)
        self.screen = screen

        self.background_col = (255, 255, 255)
        self.paint_col = (0, 0, 0)

        self.xCount = 28
        self.yCount = 28

        self.cellSize = int(boxSize/self.xCount)
        self.x_grid = np.zeros(self.xCount)
        self.y_grid = np.zeros(self.yCount)

        self.Grid = Group()

        self.create_grid()
        # Plot the grid - each cell is a rect of color white or black

    def create_grid(self):
        """Create a blank grid - or overwrite old grid with blank"""
        xPos = self.pos[0]
        yPos = self.pos[1]

        self.Grid.empty() # Ensure grid is empty before creating

        for i in range(self.xCount):
            self.x_grid[i] = xPos + i * self.cellSize

        for i in range(self.yCount):
            self.y_grid[i] = yPos + i * self.cellSize

        for i in range(self.xCount):
            for j in range(self.yCount):
                # Create each cell and append to grid group
                cell = Cell(self.screen, self.x_grid[i], self.y_grid[j], self.cellSize, i, j)
                self.Grid.add(cell)

    def check_cell_clicked(self, mouse_x, mouse_y, game_state):
        for cell in self.Grid.sprites():
            cell_clicked = cell.rect.collidepoint(mouse_x, mouse_y)
            if cell_clicked:
                cell.draw_on_cell(game_state)

    def draw_grid(self):
        for cell in self.Grid.sprites():
            cell.draw_cell()

    def convert_grid(self):
        grid = np.zeros((self.yCount, self.xCount))
        for cell in self.Grid.sprites():
            grid[cell.y_id][cell.x_id] = cell.return_drawn()
        return grid.astype(int)