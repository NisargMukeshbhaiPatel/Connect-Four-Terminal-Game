import curses

from utils.ui import draw_board, draw_rect_inside, draw_rect_around


def render_game_screen(win, state=None):
    win.nodelay(False)
    height, width = win.getmaxyx()
    xpad = 2
    ypad = 1
    board_width = 3 * width // 4
    height = height - 2 * ypad

    board_win = curses.newwin(height, board_width, ypad, xpad)
    gapx, gapy = draw_board(6, 7, board_width, height, board_win)

    draw_rect_inside(0, 1, gapx, gapy, board_win)
    draw_rect_around(4, gapx, gapy * 6, board_win, 2)
    draw_rect_around(0, gapx, gapy * 4, board_win, 4)

    def render_info_text():
        win.addstr(0, width - 27, "Select Column-> Arrow Keys", curses.color_pair(12))
        win.addstr(1, width - 27, "   Drop Piece-> Enter", curses.color_pair(12))
        win.addstr(2, width - 27, "     Go Back -> q", curses.color_pair(11))

    render_info_text()
    win.refresh()
    board_win.refresh()
    board_win.getch()
    board_win.refresh()
    while True:
        while True:
            key = board_win.getch()
            if key == curses.KEY_LEFT:
                break

            elif key == curses.KEY_RIGHT:
                break

            # elif key == curses.KEY_ENTER or key == 10 or key == 459:

            elif key == ord("q") or key == ord("Q"):
                return "START", None

