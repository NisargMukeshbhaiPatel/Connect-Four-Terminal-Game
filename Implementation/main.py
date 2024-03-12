import curses
import time

from utils import ansi, ui

def main(stdscr):
    curses.curs_set(0)
    ansi.set_init_pair_ansi_index()

    w = stdscr.getmaxyx()[1] - 20
    h = stdscr.getmaxyx()[0] - 20
    pad = 10
    win = curses.newwin(h + pad, w + pad, 5, 5)
    gapx, gapy = ui.draw_board(6, 7, w, h, win)

    ui.draw_rect_inside(0, 1, gapx, gapy, win)

    ui.draw_rect_around(4, gapx, gapy * 6, win, 2)
    time.sleep(.5)
    ui.draw_rect_around(0, gapx, gapy * 4, win, 4)
    stdscr.refresh()
    win.refresh()
    win.getch()


# if curses.has_colors():
# win.attron(curses.color_pair(2))
# win.border()
# win.attron(curses.color_pair(0))
curses.wrapper(main)
