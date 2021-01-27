import sys
import pygame
from src import click_button_functions as cb


def check_events(game_state, grid, submit_btn, clear_btn,
                 pred_window, model, grid_btn, draw_btn, erase_btn):
    """Respond to key presses and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, grid)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()

            check_buttons(game_state, grid, submit_btn, clear_btn, pred_window, model,
                          grid_btn, draw_btn, erase_btn, mouse_x, mouse_y)

            game_state.hold_mouse()
        elif event.type == pygame.MOUSEBUTTONUP:
            game_state.release_mouse()


def check_keydown_events(event, grid):
    if event.key == pygame.K_c:
        grid.create_grid()


def check_mouse_events(game_state, grid):
    if game_state.mouse_down:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        grid.check_cell_clicked(mouse_x, mouse_y, game_state)


def check_buttons(game_state, grid, submit_btn, clear_btn, pred_window, model,
                  grid_btn, draw_btn, erase_btn, mouse_x, mouse_y):
    if clear_btn.rect.collidepoint(mouse_x, mouse_y):
        cb.click_clear_button(grid, pred_window)
    elif submit_btn.rect.collidepoint(mouse_x, mouse_y):
        cb.click_submit_button(grid, pred_window, model)
    elif grid_btn.rect.collidepoint(mouse_x, mouse_y):
        cb.click_grid_button(grid_btn, grid, game_state)
    elif draw_btn.rect.collidepoint(mouse_x, mouse_y):
        cb.click_draw_button(draw_btn, erase_btn, game_state)
    elif erase_btn.rect.collidepoint(mouse_x, mouse_y):
        cb.click_erase_button(draw_btn, erase_btn, game_state)
