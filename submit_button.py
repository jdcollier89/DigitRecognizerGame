from button import Button


class SubmitButton(Button):
    def __init__(self, screen):
        self.width, self.height = 200, 50
        self.fontsize = 48
        super().__init__(screen, self.width, self.height, 48)

        # Overwrite default values
        self.text_color = (250, 250, 250)
        self.button_color = (80, 220, 80)

        self.rect.centerx = self.screen_rect.centerx - 110
        self.rect.centery = self.screen_rect.centery + 290
        self.msg = 'Submit'

        self.prep_msg()
