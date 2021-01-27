import pygame

from settings import Settings
from game_state import GameState
from model import Model
from grid import Grid
from prediction_window import PredictionWindow
from submit_button import SubmitButton
from clear_button import ClearButton
from grid_button import GridButton
from draw_button import DrawButton
from erase_button import EraseButton
import check_event_functions as ce


def draw_buttons(clear_btn, submit_btn, grid_btn, draw_btn, erase_btn):
    clear_btn.draw_button()
    submit_btn.draw_button()
    grid_btn.draw_button()
    draw_btn.draw_button()
    erase_btn.draw_button()


def run_game():
    pygame.init()

    ai_settings = Settings()
    screen = pygame.display.set_mode((
        ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Digit Recognizer')
    game_state = GameState(ai_settings)
    model = Model(0, ai_settings)

    clear_btn = ClearButton(screen)
    submit_btn = SubmitButton(screen)
    grid_btn = GridButton(screen, game_state)
    draw_btn = DrawButton(screen, game_state)
    erase_btn = EraseButton(screen, game_state)
    # Brush Size - 1/2/3

    grid = Grid(400, 25, 20, screen, game_state)
    pred_window = PredictionWindow(ai_settings, screen)

    while True: # Game Loop
        screen.fill(ai_settings.bg_color)

        ce.check_events(game_state, grid, submit_btn, clear_btn, pred_window,
                        model, grid_btn, draw_btn, erase_btn)
        ce.check_mouse_events(game_state, grid)

        grid.draw_grid()
        draw_buttons(clear_btn, submit_btn, grid_btn, draw_btn, erase_btn)
        pred_window.draw_window()
        
        pygame.display.flip()


run_game()