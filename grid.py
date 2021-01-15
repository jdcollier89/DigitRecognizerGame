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
        self.drawSize = self.cellSize - 1
        self.brushSize = 2
        self.x_grid = np.zeros(self.xCount)
        self.y_grid = np.zeros(self.yCount)

        self.Grid = Group()

        self.create_grid() # Plot the grid - each cell is a rect of color white or black

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
                cell = Cell(self.screen, self.x_grid[i], self.y_grid[j], self.drawSize, i, j)
                self.Grid.add(cell)

    def check_cell_clicked(self, mouse_x, mouse_y, game_state):
        for cell in self.Grid.sprites():
            if self.brushSize == 1:
                offset = 0
            if self.brushSize == 2:
                offset = self.cellSize/2
            elif self.brushSize == 3:
                offset = self.cellSize

            # Brush Size = 1
            #cell_clicked = cell.rect.collidepoint(mouse_x, mouse_y)

            cell_clicked1 = cell.rect.collidepoint(mouse_x-offset, mouse_y-offset)
            cell_clicked2 = cell.rect.collidepoint(mouse_x+offset, mouse_y-offset)
            cell_clicked3 = cell.rect.collidepoint(mouse_x, mouse_y-offset)

            cell_clicked4 = cell.rect.collidepoint(mouse_x-offset, mouse_y)
            cell_clicked5 = cell.rect.collidepoint(mouse_x+offset, mouse_y)
            cell_clicked6 = cell.rect.collidepoint(mouse_x, mouse_y)

            cell_clicked7 = cell.rect.collidepoint(mouse_x-offset, mouse_y+offset)
            cell_clicked8 = cell.rect.collidepoint(mouse_x+offset, mouse_y+offset)
            cell_clicked9 = cell.rect.collidepoint(mouse_x, mouse_y+offset)

            if cell_clicked1 or cell_clicked2 or cell_clicked3 or cell_clicked4 or cell_clicked5\
                    or cell_clicked6 or cell_clicked7 or cell_clicked8 or cell_clicked9:
                cell.draw_on_cell(game_state)

    def draw_grid(self):
        for cell in self.Grid.sprites():
            cell.draw_cell()

    def convert_grid(self):
        grid = np.zeros((self.yCount, self.xCount))
        for cell in self.Grid.sprites():
            grid[cell.y_id][cell.x_id] = cell.return_drawn()
        return grid.astype(int)

    def set_show_grid(self):
        self.drawSize = self.cellSize - 1

    def set_hide_grid(self):
        self.drawSize = self.cellSize

    def set_brush_size(self, brush_size):
        self.brushSize = brush_size
