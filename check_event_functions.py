import sys
import pygame


def check_events(game_state, grid, submit_btn, clear_btn):
    """Respond to key presses and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, grid)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_submit_button(submit_btn, grid, mouse_x, mouse_y)
            check_clear_button(clear_btn, grid, mouse_x, mouse_y)
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


def check_clear_button(clear_btn, grid, mouse_x, mouse_y):
    button_clicked = clear_btn.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked:
        grid.create_grid()


def check_submit_button(submit_btn, grid, mouse_x, mouse_y):
    button_clicked = submit_btn.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked:
        print("Submit Button Clicked")