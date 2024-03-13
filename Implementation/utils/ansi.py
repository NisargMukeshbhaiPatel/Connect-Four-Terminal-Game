import curses
import warnings
from ascii_magic import AsciiArt

# ANSI color codes from 30-37
ANSI_COLORS = (
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
    for i in range(10, 18):
        curses.init_pair(i, ANSI_COLORS[i - 10], -1)


def add_img_with_ansi(path, x, y, cols, stdscr):
    my_art = AsciiArt.from_image(path)
    ascii_output = my_art.to_ascii(columns=cols - 2, char=" ")

    lines = ascii_output.split("\n")
    # print("LEN->", len(lines), " AkTUAL HEIGHT->", stdscr.getmaxyx()[0])

    for i, line in enumerate(lines):
        parts = line.split("\x1b[")[1:]
        for j, part in enumerate(parts):
            idx = int(part.split("m")[0]) - 30
            # initialize color.set_init_pair_ansi_index() to access ansi indexed color-pairs
            try:
                stdscr.addch(y + i, x + j, " ", curses.color_pair(idx))
            except:
                break

        try:
            stdscr.addch("\n")
        except:
            break
