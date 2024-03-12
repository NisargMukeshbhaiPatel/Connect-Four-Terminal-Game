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



def main(stdscr):
    curses.curs_set(0)
    set_init_pair_ansi_index()

    w = stdscr.getmaxyx()[1] - 20
    h = stdscr.getmaxyx()[0] - 20
    win = curses.newwin(stdscr.getmaxyx()[0] - 10, stdscr.getmaxyx()[1] - 10, 5, 5)
    win.addstr("HELLLLLOO", curses.color_pair(4))

    win.refresh()
    win.getch()


# if curses.has_colors():
# win.attron(curses.color_pair(2))
# win.border()
# win.attron(curses.color_pair(0))
curses.wrapper(main)
