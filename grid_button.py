from button import Button


class GridButton(Button):
    def __init__(self, screen, game_state):
        self.width, self.height = 200, 30
        self.font_size = 30
        super().__init__(screen, self.width, self.height, self.font_size)

        self.rect.centerx = self.screen_rect.centerx - 110
        self.rect.centery = self.screen_rect.centery + 110
        self.button_color = (150, 150, 150)

        # Set the button message content
        self.on_grid_msg = "Toggle Grid: ON"
        self.off_grid_msg = "Toggle Grid: OFF"
        self.set_grid_msg(game_state)

    def set_grid_msg(self, game_state):
        if game_state.show_grid:
            self.msg = self.on_grid_msg
        else:
            self.msg = self.off_grid_msg
        self.prep_msg()

