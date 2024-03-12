import curses
import time

from utils import ansi, ui

def main(stdscr):
    curses.curs_set(0)
    ansi.set_init_pair_ansi_index()
    frames = 8
    for i in range(1, 15):
        i %= frames
        stdscr.clear()
        width = stdscr.getmaxyx()[1]/2 - 1
        ansi.add_img_with_ansi(f"assets/CF/CF-{i}.png", width, stdscr)
        stdscr.refresh()
        time.sleep(.5)


# if curses.has_colors():
# win.attron(curses.color_pair(2))
# win.border()
# win.attron(curses.color_pair(0))
curses.wrapper(main)
