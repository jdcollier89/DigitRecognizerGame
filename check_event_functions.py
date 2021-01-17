import sys
import pygame


def check_events(game_state, grid, submit_btn, clear_btn, pred_window, model, grid_btn, draw_btn, erase_btn):
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
            check_grid_button(grid_btn, grid, game_state, mouse_x, mouse_y)
            check_draw_button(draw_btn, erase_btn, game_state, mouse_x, mouse_y)
            check_erase_button(draw_btn, erase_btn, game_state, mouse_x, mouse_y)

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


def check_grid_button(grid_btn, grid, game_state, mouse_x, mouse_y):
    button_clicked = grid_btn.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked:
        if game_state.show_grid:
            grid.set_hide_grid()
            game_state.show_grid = False
        else:
            grid.set_show_grid()
            game_state.show_grid = True
        grid_btn.set_grid_msg(game_state)


def check_draw_button(draw_btn, erase_btn, game_state, mouse_x, mouse_y):
    button_clicked = draw_btn.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked:
        game_state.set_draw()
        draw_btn.set_button_active()
        erase_btn.set_button_inactive()


def check_erase_button(draw_btn, erase_btn, game_state, mouse_x, mouse_y):
    button_clicked = erase_btn.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked:
        game_state.set_erase()
        draw_btn.set_button_inactive()
        erase_btn.set_button_active()


## Create check_button function
# Will Check all buttons for a press
# Then call the 'button clicked' actions of relevant button