import pygame.font


class PredictionWindow:
    """A class to contain the prediction made by the model"""

    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings

        self.width, self.height = 420, 100
        self.win_color = (100, 100, 100)

        # Font settings
        self.text_color = (250, 250, 250)
        self.font = pygame.font.SysFont(None, 20)

        # Prep the blank opening window
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery + 180
        self.reset_window()

    def prep_window(self, msg):
        """"Create a screen rect and text"""
        self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.win_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def reset_window(self):
        """Set the window to contain no message"""
        self.prep_window("")

    def update_window(self, class_pred, pred_score):
        """Set the prediction message inside the message box"""
        msg = "I think you drew a {}. I am {:.0f}% confident!".format(class_pred, pred_score)
        self.prep_window(msg)

    def draw_window(self):
        """Draw blank window and then draw message on the screen"""
        self.screen.fill(self.win_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)