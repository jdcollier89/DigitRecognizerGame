class Settings:

    def __init__(self):
        """Initialize the game's static settings."""

        # Screen Settings
        self.screen_width = 440
        self.screen_height = 600
        self.bg_color = (50, 50, 50)
        self.box_color = (255, 255, 255)

        # Drawing box
        self.box_width = 1000
        self.box_height = 500

        self.model_path = 'mnist_model.model'

        self.show_grid = True
