import sys
import pygame


def check_events(game_state, grid, submit_btn, clear_btn, pred_window, model):
    """Respond to key presses and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, grid)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_submit_button(submit_btn, grid, pred_window, mouse_x, mouse_y, model)
            check_clear_button(clear_btn, grid, pred_window, mouse_x, mouse_y)
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


def check_clear_button(clear_btn, grid, pred_window, mouse_x, mouse_y):
    button_clicked = clear_btn.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked:
        grid.create_grid()
        pred_window.reset_window()


def check_submit_button(submit_btn, grid, pred_window, mouse_x, mouse_y, model):
    button_clicked = submit_btn.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked:
        array = grid.convert_grid()
        class_pred, pred_score = model.predict_class(array)
        pred_window.update_window(class_pred, pred_score)