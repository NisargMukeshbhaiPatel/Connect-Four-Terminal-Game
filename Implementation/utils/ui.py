# This File contains all the ui related functions that could be used not just in connect-four but also any grid/cell type game
# TODO remove curses.color
import curses
import warnings


def draw_board(rows, cols, width, height, win):
    flag = False
    gapx = width // cols
    gapy = height // rows
    width = gapx * cols

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


def add_multi_line_str(win, y, x, str, color=None):
    lines = str.split("\n")
    for i, line in enumerate(lines):
        if color is not None:
            win.addstr(y + i, x, line, color)
        else:
            win.addstr(y + i, x, line)
