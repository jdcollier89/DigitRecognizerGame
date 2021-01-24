def click_clear_button(grid, pred_window):
    grid.create_grid()
    pred_window.reset_window()


def click_submit_button(grid, pred_window, model):
    array = grid.convert_grid()
    class_pred, pred_score = model.predict_class(array)
    pred_window.update_window(class_pred, pred_score)


def click_grid_button(grid_btn, grid, game_state):
    if game_state.show_grid:
        grid.set_hide_grid()
        game_state.show_grid = False
    else:
        grid.set_show_grid()
        game_state.show_grid = True
    grid_btn.set_grid_msg(game_state)


def click_draw_button(draw_btn, erase_btn, game_state):
    game_state.set_draw()
    draw_btn.set_button_active()
    erase_btn.set_button_inactive()


def click_erase_button(draw_btn, erase_btn, game_state):
    game_state.set_erase()
    draw_btn.set_button_inactive()
    erase_btn.set_button_active()