import curses
import time

from utils import ansi, ui
from assets import ascii


def add_multi_line_str(win, y, x, str, color=None):
    lines = str.split("\n")
    for i, line in enumerate(lines):
        if color is not None:
            win.addstr(y + i, x, line, color)
        else:
            win.addstr(y + i, x, line)


def main(stdscr):
    curses.curs_set(0)
    ansi.set_init_pair_ansi_index()

    stdscr.refresh()
    add_multi_line_str(stdscr, 6, 5, ascii.CONNECT_FOUR_LOGO)
    stdscr.refresh()
    stdscr.getch()


# if curses.has_colors():
# win.attron(curses.color_pair(2))
# win.border()
# win.attron(curses.color_pair(0))
curses.wrapper(main)
