import curses

from utils.ansi import set_init_pair_ansi_index
from screens.start_screen import render_start_screen


def main(stdscr):
    curses.curs_set(0)
    set_init_pair_ansi_index()

     
    action = render_start_screen(stdscr)
    if action == "PLAY":
        print(action)
    elif action == "HOW_TO_PLAY":
        print(action)


# if curses.has_colors():
# win.attron(curses.color_pair(2))
# win.border()
# win.attron(curses.color_pair(0))
curses.wrapper(main)
