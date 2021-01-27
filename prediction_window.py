import pygame.font


class PredictionWindow:
    """A class to contain the prediction made by the model"""

    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings

        self.width, self.height = 420, 120
        self.win_color = (100, 100, 100)

        # Font settings
        self.text_color = (250, 250, 250)

        # Prep the blank opening window
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery + 195
        self.reset_window()

    def prep_window(self, msg1, msg2, msg3):
        """"Create a screen rect and text"""
        self.font = pygame.font.SysFont(None, 20)
        self.msg_image1 = self.font.render(msg1, True, self.text_color)
        self.msg_image_rect1 = self.msg_image1.get_rect()
        self.msg_image_rect1.centerx = self.rect.centerx
        self.msg_image_rect1.centery = self.rect.centery - 45

        self.font = pygame.font.SysFont(None, 85)
        self.msg_image2 = self.font.render(msg2, True, self.text_color)
        self.msg_image_rect2 = self.msg_image2.get_rect()
        self.msg_image_rect2.center = self.rect.center

        self.font = pygame.font.SysFont(None, 20)
        self.msg_image3 = self.font.render(msg3, True, self.text_color)
        self.msg_image_rect3 = self.msg_image3.get_rect()
        self.msg_image_rect3.centerx = self.rect.centerx
        self.msg_image_rect3.centery = self.rect.centery + 45

    def reset_window(self):
        """Set the window to contain no message"""
        self.prep_window("", "", "")

    def update_window(self, class_pred, pred_score):
        """Set the prediction message inside the message box"""
        msg1 = "I think you drew a"
        msg2 = str(class_pred)
        msg3 = "I am {:.0f}% confident!".format(pred_score)
        self.prep_window(msg1, msg2, msg3)

    def draw_window(self):
        """Draw blank window and then draw message on the screen"""
        self.screen.fill(self.win_color, self.rect)
        self.screen.blit(self.msg_image1, self.msg_image_rect1)
        self.screen.blit(self.msg_image2, self.msg_image_rect2)
        self.screen.blit(self.msg_image3, self.msg_image_rect3)