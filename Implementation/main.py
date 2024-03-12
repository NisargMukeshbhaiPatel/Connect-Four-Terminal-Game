import curses

import time

ANSI_COLORS = (
    # ANSI color codes from 30-37
	curses.COLOR_BLACK,  # 30
	curses.COLOR_RED,
	curses.COLOR_GREEN,
	curses.COLOR_YELLOW,
	curses.COLOR_BLUE,
	curses.COLOR_MAGENTA,
	curses.COLOR_CYAN,
	curses.COLOR_WHITE,  # 37
)

def set_init_pair_ansi_index():
	curses.use_default_colors()
	# Set pairs according to ANSI_COLORS idx
	# For 0, it's set to default background color of terminal and also curses doesn't allow setting it
	for i in range(1, 8):
		curses.init_pair(i, -1, ANSI_COLORS[i])


# TODO handle x overflow
def draw_board(rows, cols, width, height, win):
    gapx = width // cols
    gapy = height // rows + 1

    # Horizontal lines
    for i in range(0, rows + 1):
        for j in range(0, width):
            try:
                win.addch(i * gapy, j, " ", curses.color_pair(4))
            except:
                break

    # Vertical lines (height + pad so last row will have extra |)
    for i in range(0, height + 3):
        for j in range(0, cols + 1):
            try:
                win.addch(i, j * gapx, " ", curses.color_pair(4))
            except:
                break

    return [gapx, gapy]


def main(stdscr):
    curses.curs_set(0)
    set_init_pair_ansi_index()

    w = stdscr.getmaxyx()[1] - 20
    h = stdscr.getmaxyx()[0] - 20
    pad = 10
    win = curses.newwin(h + pad, w + pad, 5, 5)
    gapx, gapy = draw_board(6, 7, w, h, win)
    win.refresh()
    win.getch()


# if curses.has_colors():
# win.attron(curses.color_pair(2))
# win.border()
# win.attron(curses.color_pair(0))
curses.wrapper(main)
