from button import Button


class DrawButton(Button):
    def __init__(self, screen, game_state):
        self.width, self.height = 80, 30
        self.fontsize = 30
        super().__init__(screen, self.width, self.height, self.fontsize)

        self.active_button_color = (80, 220, 80)
        self.inactive_button_color = (150, 150, 150)
        if game_state.draw_active:
            self.button_color = self.active_button_color

        self.rect.centerx = self.screen_rect.centerx + 80
        self.rect.centery = self.screen_rect.centery + 110

        self.msg = "Draw"
        self.prep_msg()

    def set_button_active(self):
        self.button_color = self.active_button_color

    def set_button_inactive(self):
        self.button_color = self.inactive_button_color