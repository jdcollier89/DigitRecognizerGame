
class GameState:
    def __init__(self):
        self.mouse_down = False
        self.draw_color = (0, 0, 0)

    def hold_mouse(self):
        self.mouse_down = True

    def release_mouse(self):
        self.mouse_down = False

    def set_draw(self):
        self.draw_color = (0, 0, 0)

    def set_erase(self):
        self.draw_color = (255, 255, 255)