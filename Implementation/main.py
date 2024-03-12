import curses

import time
from utils import ansi

# TODO handle x overflow
def draw_board(rows, cols, width, height, win):
    flag = False
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
                flag = True
                break
    if flag:
        warnings.warn("Attempted to draw game board in insufficient win space")

    return [gapx, gapy]

def draw_rect_inside(row, col, w, h, win):
    x = col + 1 if col == 0 else col * w + 1
    y = row + 1 if row == 0 else row * h + 1
    flag = False

    for i in range(y, y + h - 1):
        for j in range(x, x + w - 1):
            try:
                win.addch(i, j, " ", curses.color_pair(3))
            except:
                flag = True
                break
    if flag:
        warnings.warn("Attempted to draw_rect_inside insufficient win space")


def draw_rect_around(col, w, h, win, color_pair_idx):
    flag = False
    x = col * w
    y = 0
    # i -> rows, j -> cols
    for i in range(y, y + h + 1):
        for j in range(x, x + w + 1):
            # Basically add full line for 1st and last row
            # and for middle just add on 1st and last column
            if i == y or i == y + h or j == x or j == x + w:
                try:
                    win.addch(i, j, " ", curses.color_pair(color_pair_idx))
                except:
                    flag = True
                    break
    if flag:
        warnings.warn("Attempted to draw_rect_around insufficient space")


def main(stdscr):
    curses.curs_set(0)
    ansi.set_init_pair_ansi_index()

    w = stdscr.getmaxyx()[1] - 20
    h = stdscr.getmaxyx()[0] - 20
    pad = 10
    win = curses.newwin(h + pad, w + pad, 5, 5)
    gapx, gapy = draw_board(6, 7, w, h, win)

    draw_rect_inside(0, 1, gapx, gapy, win)

    draw_rect_around(4, gapx, gapy * 6, win, 2)
    time.sleep(.5)
    draw_rect_around(0, gapx, gapy * 4, win, 4)
    stdscr.refresh()
    win.refresh()
    win.getch()


# if curses.has_colors():
# win.attron(curses.color_pair(2))
# win.border()
# win.attron(curses.color_pair(0))
curses.wrapper(main)
