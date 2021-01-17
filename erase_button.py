import pygame.font


class EraseButton:

    def __init__(self, screen, game_state):
        """Initialize the buttons attributes"""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Set the dimensions and properties of the button
        self.width, self.height = 80, 30
        self.text_color = (250, 250, 250)
        self.font = pygame.font.SysFont(None, 30) # Default font at size 48

        self.active_button_color = (80, 220, 80)
        self.inactive_button_color = (150, 150, 150)
        if game_state.draw_active:
            self.button_color = self.inactive_button_color

        # Build the button's rect object
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.centerx = self.screen_rect.centerx + 170
        self.rect.centery = self.screen_rect.centery + 90

        # Set the button message content
        self.msg = "Erase"
        self.prep_msg()

    def set_button_active(self):
        self.button_color = self.active_button_color

    def set_button_inactive(self):
        self.button_color = self.inactive_button_color

    def prep_msg(self):
        """Turn msg into a rendered image and center text on the button"""
        self.msg_image = self.font.render(self.msg, True, self.text_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """Draw blank button and then draw message on the screen"""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)