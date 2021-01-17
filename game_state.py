
class GameState:
    def __init__(self):
        self.mouse_down = False
        self.show_grid = True
        self.set_draw()

    def hold_mouse(self):
        self.mouse_down = True

    def release_mouse(self):
        self.mouse_down = False

    def set_draw(self):
        self.draw_active = True
        self.draw_color = (0, 0, 0)

    def set_erase(self):
        self.draw_active = False
        self.draw_color = (255, 255, 255)