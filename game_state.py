
class GameState:
    def __init__(self, settings):
        self.mouse_down = False
        self.show_grid = True
        self.paint_color = settings.paint_color
        self.erase_color = settings.grid_color

        self.set_draw()

    def hold_mouse(self):
        self.mouse_down = True

    def release_mouse(self):
        self.mouse_down = False

    def set_draw(self):
        self.draw_active = True
        self.draw_color = self.paint_color

    def set_erase(self):
        self.draw_active = False
        self.draw_color = self.erase_color