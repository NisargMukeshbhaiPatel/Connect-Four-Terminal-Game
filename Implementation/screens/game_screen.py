import curses
import time

from utils.ui import draw_board, draw_rect_inside, draw_rect_around
from game import game_logic as game


def render_game_screen(win, state=None):
    win.nodelay(True)
    # Calc dimensions
    height, width = win.getmaxyx()
    xpad = 2
    ypad = 1
    board_width = 3 * width // 4
    height = height - 2 * ypad

    # Game will be 6 X 7
    rows = 6
    cols = 7
    board_win = curses.newwin(height, board_width, ypad, xpad)
    board_win.keypad(True)
    board_win.clear()
    gapx, gapy = draw_board(rows, cols, board_width - xpad, height, board_win, 0.008)


    # Initialize the Game
    game_state = game.create_connect_four_game(
        "Player 1", curses.color_pair(3), "Player 2", curses.color_pair(1), rows, cols
    )

    def render_player_turn(name, color):
        win.addstr(3 * gapy - 1, 8 * gapx - 1, f"{name}'s Turn")
        draw_rect_inside(3, 8, gapx, gapy, color, win)
        win.refresh()
    # render 1st player turn
    render_player_turn("Player 1", curses.color_pair(3))

    # Set current column
    curr_column = 3
    draw_rect_around(curr_column, gapx, gapy * 6, board_win, curses.color_pair(2))

    def update_col(prev_col):
        draw_rect_around(prev_col, gapx, gapy * 6, board_win, curses.color_pair(4))
        draw_rect_around(curr_column, gapx, gapy * 6, board_win, curses.color_pair(2))
        board_win.refresh()

    def flash_winning_cols(cells, color, delay=.1):
        for i in range(18):
            for row, col in cells:
                if i % 2 == 0:
                    draw_rect_inside(row, col, gapx, gapy, curses.color_pair(7), board_win)
                else:
                    draw_rect_inside(row, col, gapx, gapy, color, board_win)
            time.sleep(delay)
            board_win.refresh()

    def render_info_text():
        text_length = 27
        win.addstr(
            0, width - text_length, "Select Column-> Arrow Keys", curses.color_pair(12)
        )
        win.addstr(
            1, width - text_length, "   Drop Piece-> Enter", curses.color_pair(12)
        )
        win.addstr(2, width - text_length, "     Go Back -> q", curses.color_pair(11))

    render_info_text()
    win.refresh()
    board_win.refresh()

    while True:
        key = board_win.getch()
        win.refresh()
        if key == curses.KEY_RIGHT:
            prev_col = curr_column
            curr_column += 1
            curr_column %= cols
            update_col(prev_col)

        elif key == curses.KEY_LEFT:
            prev_col = curr_column
            curr_column -= 1
            if curr_column < 0:
                curr_column = cols - 1
            update_col(prev_col)

        elif key == curses.KEY_ENTER or key == 10 or key == 459:
            curr_row = game.drop_piece(game_state, curr_column)
            player = game.get_current_player(game_state)
            player_idx = game_state["turn"]

            if curr_row != -1:
                draw_rect_inside(curr_row, curr_column, gapx, gapy, player["color"], board_win)
                board_win.refresh()

                winning_cells = game.check_win(
                    game_state["game_board"], curr_row, curr_column, player_idx
                )
                if len(winning_cells):
                    flash_winning_cols(winning_cells, player["color"])
                    return "START", player

                elif game.check_draw(game_state["game_board"]):
                    print("DRAWW IS NOT HANDLED")
                    # TODO handle if game is DRAW

                else:
                    game.switch_turn(game_state)
                    player = game.get_current_player(game_state) # player after switch_turn
                    render_player_turn(player["name"], player["color"])

        elif key == ord("q") or key == ord("Q"):
            return "START", None
