import pygame
from settings import Settings
import check_event_functions as ce
from grid import Grid
from game_state import GameState
from button import Button

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((
        ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Digit Recognizer')
    game_state = GameState()

    clear_btn = Button(screen, 'Clear', 'c')
    submit_btn = Button(screen, 'Submit', 's')

    grid = Grid(400, 25, 25, screen)

    while True:
        screen.fill(ai_settings.bg_color)

        ce.check_events(game_state, grid, submit_btn, clear_btn)
        ce.check_mouse_events(game_state, grid)

        grid.draw_grid()
        clear_btn.draw_button()
        submit_btn.draw_button()
        
        pygame.display.flip()


run_game()