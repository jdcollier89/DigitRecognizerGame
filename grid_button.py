import pygame.font


class GridButton:

    def __init__(self, screen, game_state):
        """Initialize the buttons attributes"""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Set the dimensions and properties of the button
        self.width, self.height = 200, 30
        self.text_color = (250, 250, 250)
        self.font = pygame.font.SysFont(None, 30) # Default font at size 48
        self.button_color = (150, 150, 150)

        # Build the button's rect object
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.centerx = self.screen_rect.centerx - 110
        self.rect.centery = self.screen_rect.centery + 90

        # Set the button message content
        self.on_grid_msg = "Toggle Grid: ON"
        self.off_grid_msg = "Toggle Grid: OFF"
        self.set_grid_msg(game_state)
        self.prep_msg()

    def set_grid_msg(self, game_state):
        if game_state.show_grid:
            self.msg = self.on_grid_msg
        else:
            self.msg = self.off_grid_msg
        self.prep_msg()

    def prep_msg(self):
        """Turn msg into a rendered image and center text on the button"""
        self.msg_image = self.font.render(self.msg, True, self.text_color,
                                          self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """Draw blank button and then draw message on the screen"""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
